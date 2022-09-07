"""
RNN pytorch 简洁实现
"""


import torch
from torch import nn

# 1. 输入数据 Embedding
input = [[[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 1, 2, 5], [4, 3, 2, 4, 0]],
         [[1, 0, 2, 3, 6], [2, 1, 2, 0, 3], [2, 4, 1, 2, 5], [0, 2, 3, 0, 1]],
         [[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 5, 1, 2], [4, 3, 2, 4, 0]]]
input = torch.tensor(input, dtype=torch.float32)
label = torch.tensor([1, 0, 1])
print(label)
print(input.shape)
"""
# 3是表示3句话，4表示每句话4个字，5表示每个字用5维(5个数)表示
# 批量大小, 句子长度, 词嵌入大小
# 批量大小, 句子长度, 词嵌入大小 --> 句子长度, 批量大小, 词嵌入大小 
"""
input = input.transpose(1, 0)
print(input.shape)

# 2. RNN 网络
"""
设计两层，每一层6个神经元，单向 RNN 网络
"""
hidden_size = 6                  # 一层6个神经元
embedding_len = input.shape[2]   # =5 ,每个字用5个数字表示
dropout = 0.5
num_layer = 2


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()
        self.rnn = nn.RNN(input_size = embedding_len,        # 输入input的特征大小
                          hidden_size = hidden_size,         # 隐藏层h的特征大小(神经元个数)
                          num_layers = num_layer,            # RNN层数
                          nonlinearity='relu',               # 激活函数
                          bidirectional=False,               # True设置为RNN为双向
                          batch_first=False,    # 设置为True之后
                                                # 输入输出为(batch_size, seq_len, input_size)
                          dropout=dropout)
        self.linear1 = nn.Linear(6, 200)
        self.linear2 = nn.Linear(200, 2)

    def forward(self, input):
        # input：(seq_len，batch_size，input_size)
        # hidden0：（num_layers * directions，batch_size，hidden_size）
        output, hidden = self.rnn(input)  # 单向RNN output[-1] = hidden[-1]
        # output：(seq_len, batch_size, hidden_size * directions)  保存最后一层每个时刻隐藏层的值
        # hidden：(num_layers * directions, batch_size, hidden_size)  保存每一层最后时刻隐藏层的值
        x2 = self.linear1(output[-1])
        x2 = self.linear2(x2)
        return x2


# 3. RNN 模型定义
net = RNN()
lr = 1e-3   # 学习率
optimizer = torch.optim.Adam(net.parameters(), lr)  # 优化算法
loss = nn.CrossEntropyLoss()    # 损失函数

# 4. 训练模型
epoch = 1000               # 迭代1000次
for i in range(epoch):
    pred = net(input)       # 预测
    l = loss(pred, label)   # 计算损失
    optimizer.zero_grad()   # 梯度归零
    l.backward()            # 反向传播
    optimizer.step()        # 梯度更新
    if i % 100 == 0:
        print(l.item())