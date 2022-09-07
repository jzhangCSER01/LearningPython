"""
使用卷积神经网络 手写数字识别
"""


import matplotlib
from matplotlib import pyplot as plt
import torch
from torch import nn
import torchvision  # 帮助图像处理库文件

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# 1. 手写数字识别数据集 黑白图片 只有一个通道
batch_size = 32  # 每个批次 32 个数据
# 下载数据集
train_data = torchvision.datasets.MNIST("./data/mnist_data", train=True, download=True,
                                       transform=torchvision.transforms.Compose([
                                           torchvision.transforms.ToTensor()
                                       ]))
train_loader = torch.utils.data.DataLoader(train_data,
                                               batch_size = batch_size,  # batch 大小
                                               shuffle = True,           # 是否打乱数据顺序
                                               num_workers = 0,
                                               pin_memory = True)
test_data = torchvision.datasets.MNIST("./data/mnist_data", train=False, download=True,
                                       transform=torchvision.transforms.Compose([
                                           torchvision.transforms.ToTensor()
                                       ]))
test_loader = torch.utils.data.DataLoader(test_data,
                                               batch_size = batch_size,
                                               shuffle = True,
                                               num_workers = 0,
                                               pin_memory = True)


# 2. 定义卷积神经网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 数据集图片是黑白图片 只有一个通道 输入 in_channels = 1
        # out_channels = 4 定义第一层卷积有 4 个卷积核，每个卷积核大小是(3x3)
        # 卷积前，选择填充矩阵，填充范围，周围 1
        self.Conv1 = nn.Conv2d(in_channels=1, out_channels=4, kernel_size=(3, 3), padding=1)
        # 池化窗口大小 (2, 2), 步长为 1
        self.MaxPooling1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        # 因为第一层卷积用了 4 个卷积核，所以生成了 4 个通道，这里每个卷积核就需要定义成(4x3x3)
        # out_channels=8 代表有 8 个卷积核，输出通道也为 8, 也就是能得到 8 个矩阵
        self.Conv2 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=(3, 3), padding=1)
        self.MaxPooling2 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        # 全连接层
        self.linear3 = nn.Linear(8 * 7 * 7, 100)
        self.linear4 = nn.Linear(100, 10)

    def forward(self, x):              # 32 代表每个批次大小为 32，表示有 32 个数据一起运算
        x = torch.relu(self.Conv1(x))  # (32x1x28x28) -> (32x4x28x28)
        x = self.MaxPooling1(x)        # (32x4x28x28) -> (32x4x14x14)
        x = torch.relu(self.Conv2(x))  # (32x4x14x14) -> (32x8x14x14)
        x = self.MaxPooling2(x)        # (32x8x14x14)   -> (32x8x7x7)
        x = x.view(-1, 8 * 7 * 7)      # (32x8x7x7)   -> (32x392)
        x = self.linear3(x)            # (32x392)     -> (32x100)
        x = self.linear4(x)            # (32x100)     -> (32x10)
        return x


# 3. 初始化网络
lr = 0.01
momentum = 0.5
model = Net()   # 定义网络
model = model.to(device)               # 把网络加载到GPU上
optimizer = torch.optim.SGD(model.parameters(), lr, momentum = momentum)    # 定义梯度优化算法
loss = nn.CrossEntropyLoss()     # 定义损失函数
print(model)                     # 打印网络结构


# 4. 训练网络
epoch = 10


def train_model(model, data_loader, loss, optimezer):
    model.train()
    train_ls = []
    it = 0
    for i in range(epoch):
        l = 0.
        for j, (data, label) in enumerate(data_loader):
            data, label = data.to(device), label.to(device)
            # data = data.squeeze().view(-1,28*28)
            # 预测结果 pre
            pre = model(data)
            count = torch.sum(pre.argmax(dim = 1).view(-1) == label.view(-1)).item()
            l = loss(pre, label)
            optimezer.zero_grad()
            l.backward()
            optimezer.step()
            if j % 100 == 0:
                it += 1
                # print("train_model: count:",loss.item(), count)
                train_ls.append(l.item())
    print("Loss图")
    plt.plot(range(it), train_ls)
    plt.show()


train_model(model, train_loader, loss, optimizer)


# 5. 测试网络
def test_model(model, test_loader, loss):
    model.eval()
    l = 0.
    count = 0
    for j, (data, label) in enumerate(test_loader):
        data, label = data.to(device), label.to(device)
        # 预测结果 pre
        pre = model(data)
        # 预测正确个数累加
        count += torch.sum(pre.argmax(dim = 1) == label).item()
        l += loss(pre, label)
    print(f"准确率:{count/len(test_data)};   loss：{l/len(test_data)}")


test_model(model, test_loader, loss)