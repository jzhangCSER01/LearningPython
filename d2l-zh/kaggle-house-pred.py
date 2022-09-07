"""
kaggle 竞赛 房价预测
数据下载、预处理、模型设置、训练、测试、结果提交
"""


import matplotlib
from matplotlib import pyplot as plt
import numpy
import torch
from torch import nn
import pandas as pd
import os
import requests
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# 0. 数据下载 第一次使用时去掉这段代码注释
# DATA_URL = 'http://d2l-data.s3-accelerate.amazonaws.com/kaggle_house_pred_train.csv'
# r = requests.get(DATA_URL, stream=True, verify=True)
# with open("./data/kaggle_house_pred_train.csv", 'wb') as f:
#     f.write(r.content)
#
# DATA_URL = 'http://d2l-data.s3-accelerate.amazonaws.com/kaggle_house_pred_test.csv'
# r = requests.get(DATA_URL, stream=True, verify=True)
# with open("./data/kaggle_house_pred_test.csv", 'wb') as f:
#     f.write(r.content)


# 1. 数据预处理

# 读取数据
train_data = pd.read_csv('./data/kaggle_house_pred_train.csv')
test_data = pd.read_csv('./data/kaggle_house_pred_test.csv')
# 把去掉 id(第 0 列) 的数据拼在一起，去掉 id 的目的是为了防止模型通过记住编号得到对应房价
all_features = pd.concat((train_data.iloc[:, 1: -1], test_data.iloc[: , 1:]))
print("train_data.shape:", train_data.shape)
print("test_data.shape:", test_data.shape)
print("all_features:", all_features.shape)
print(train_data.iloc[:5, :8])
"""
output
train_data.shape: (1460, 81)    # 训练数据有1460条，加上序号有81个属性 最后一列是 SalePrice
test_data.shape: (1459, 80)     # 测试数据有1459条，加上序号有80个属性
all_features: (2919, 79)        # 训练+测试一共2919条数据，去掉Id和房价一共79个属性
   Id  MSSubClass MSZoning  LotFrontage  LotArea Street Alley LotShape
0   1          60       RL         65.0     8450   Pave   NaN      Reg
1   2          20       RL         80.0     9600   Pave   NaN      Reg
2   3          60       RL         68.0    11250   Pave   NaN      IR1
3   4          70       RL         60.0     9550   Pave   NaN      IR1
4   5          60       RL         84.0    14260   Pave   NaN      IR1
"""

# 处理缺省值和属性

# 提取全是数字的特征索引名
numeric_features = all_features.dtypes[all_features.dtypes != 'object'].index
print(numeric_features)

# 对数据做标准化处理, 对应位置赋值
all_features[numeric_features] = all_features[numeric_features].apply(lambda x: (x - x.mean()) / (x.std()))

# 在标准化数据之后， 将缺失值设置为0
all_features[numeric_features] = all_features[numeric_features].fillna(0)

# 'Dummy_na=True' 将“na”（缺失值）视为有效的特征值，并为其创建指示符特征
#  pandas.get_dummies 把特征为类别值或离散值分成每一个特征为一个类别
all_features = pd.get_dummies(all_features, dummy_na=True)
print("all_features.shape:", all_features.shape)    # all_features.shape: (2919, 331) # 一共2919条数据，每一条331个数据 one-hot encoding


# 分成训练数据和测试数据
n_train = train_data.shape[0]
train_features = torch.tensor(all_features[:n_train].values, dtype=torch.float32)
test_features = torch.tensor(all_features[n_train:].values, dtype=torch.float32)
train_labels = torch.tensor(train_data.SalePrice.values.reshape(-1, 1), dtype=torch.float32)
print("train_features.shape:", train_features.shape)
print("train_features.shape:", test_features.shape)
print("train_labels:", train_labels.shape)

# 数据分批
batch_size = 32
dataset = torch.utils.data.TensorDataset(train_features, train_labels)
train_loader = torch.utils.data.DataLoader(dataset,                   # 数据
                                          batch_size = batch_size,    # 每个batch大小
                                          shuffle = True,             # 是否打乱数据
                                          num_workers = 0,            # 工作线程
                                          pin_memory = True)
print(f"每一批{len(next(iter(train_loader))[0])}个，一共{len(train_loader)}批")


# 3. 定义网络
class Net(nn.Module):
    def __init__(self, input, hiden0, hiden1, output):
        super().__init__()
        self.linear1 = nn.Linear(input, hiden0)
        self.linear2 = nn.Linear(hiden0, hiden1)
        self.linear3 = nn.Linear(hiden1, output)

    def forward(self, data):
        x = self.linear1(data)
        x = torch.relu(x)
        x = self.linear2(x)
        x = torch.relu(x)
        x = self.linear3(x)
        return x


# 4. 初始化神经网络

# 取出输入特征个数
in_features = train_features.shape[1]
hidden0, hidden1, out_put = 200, 100, 1
model = Net(in_features, hidden0, hidden1, out_put).to(device)

# 损失函数 loss(xi,yi)=(xi−yi)2 平方损失
loss = torch.nn.MSELoss()

# 梯度优化算法
lr = 1e-2
optimizer = torch.optim.Adam(model.parameters(), lr)

print("in_features:", in_features)
print("in_features:", train_features.shape)
print(model)


# 5. 训练神经网络
epochs = 200


def train(train_loader):
    train_ls = []
    for epoch in range(epochs):
        loss_sum = 0
        for train_batch, labels_batch in train_loader:
            train_batch, labels_batch = train_batch.to(device), labels_batch.to(device)
            # preds = torch.clamp(model(train_batch), 1, float('inf'))
            # l = loss(torch.log(preds), torch.log(labels_batch))
            l = loss(model(train_batch), labels_batch)
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
            loss_sum += l.item()
        train_ls.append(loss_sum)
    plt.plot(range(epochs), train_ls)
    plt.show()


train(train_loader)


# 6. 测试神经网络生成提交数据
def test(test_features):
    test_features = test_features.to(device)
    preds = model(test_features).detach().to("cpu").numpy()
    print(preds.squeeze().shape)

    # pandas.Series 创建新维度
    test_data['SalePrice'] = pd.Series(preds.squeeze())

    # axis选择拼接的维度
    return pd.concat([test_data['Id'], test_data['SalePrice']], axis=1)


submission = test(test_features)
submission.to_csv('./data/submission.csv', index=False)