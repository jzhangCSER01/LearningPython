"""
纯 numpy 实现 RNN
"""


import numpy as np

# 1. 词嵌入Embedding
"""
# 我是学生 -> [[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 1, 2, 5], [4, 3, 2, 4, 0]]
# 我爱学习 -> [[1, 0, 2, 3, 6], [2, 1, 2, 0, 3], [2, 4, 1, 2, 5], [0, 2, 3, 0, 1]]
# 我是男生 -> [[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 5, 1, 2], [4, 3, 2, 4, 0]]
"""
input = [[[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 1, 2, 5], [4, 3, 2, 4, 0]],
         [[1, 0, 2, 3, 6], [2, 1, 2, 0, 3], [2, 4, 1, 2, 5], [0, 2, 3, 0, 1]],
         [[1, 0, 2, 3, 6], [1, 2, 0, 2, 4], [2, 4, 5, 1, 2], [4, 3, 2, 4, 0]]]
input = np.array(input)
print(input.shape)     # 批量大小, 矩阵长度, 词嵌入大小
# 3是表示3句话，4表示每一句4个字，5表示每个字用5维(5个数)表示

# 2. 输入数据交换维度
"""
# 把第 0 轴和第 1 轴交换，也就是把句子长度放在前面。因为 RNN 是一字一个字的输入
# 这样交换后，for x in input: x就是每个句子的第一个字
# 批量大小, 句子长度, 词嵌入大小 --> 句子长度, 批量大小, 词嵌入大小
"""
input = input.transpose((1, 0, 2))
print(input.shape)  # (4, 3, 5) --> 句子长度, 批量大小, 词嵌入大小

# 3. 参数设置
batch = input.shape[1]           # =3  每个批次里有3句话
embedding_len = input.shape[2]   # =5  每个字用5个数字表示
hidden_size = 6                  # 一层6个神经元

W_xh = np.random.random((embedding_len, hidden_size))  # (5, 6)
W_hh = np.random.random((hidden_size, hidden_size))    # (6, 6)
W_hq = np.random.random((hidden_size, embedding_len))  # (6, 5)
H = np.random.random((batch, hidden_size))             # (3, 6)

params = (W_xh, W_hh, W_hq)

# 3. RNN 网络定义


def rnn(inputs, H, params):
    # inputs 的形状: (句子长度，批量大小, 词嵌入大小)
    W_xh, W_hh, W_hq  = params
    outputs = []
    # X 的形状: (批量大小, 词嵌入大小) 句子长度为4，循环 4 次
    for X in inputs:
        # 第 i 循环，同时输入每个句子的第i个字的词嵌入
        H = np.maximum(np.matmul(X, W_xh) + np.matmul(H, W_hh), 0)
        Y = np.matmul(H, W_hq)
        outputs.append(Y)
    return np.array(outputs), H
outputs, H = rnn(input, H, params)
print(outputs)
print(outputs.shape)
print(H.shape)