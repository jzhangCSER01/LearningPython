"""
实现神经网络的基本步骤:
1、整理数据集。2、定义神经网络。3、设置超参数，学习率。4、选择优化算法。5、定义loss。6、反向传播求梯度。7、更新梯度。8、测试网络。
纯 numpy 实现三层深度神经网络
用 3 层神经网络拟合出 label = data[0] + data[1] 的加法运算，最后测试 0.1+0.5 的结果
"""


import numpy as np
from matplotlib import pyplot as plt

# 设置模型大小
input, hide_1, hide_2, output = 2, 5, 4, 1

# 生成 200 个数据
# 每一个数据由两个数字组成，标签为两个数的和
data = np.random.random(size=(200, 2))
w = [1, 1]
label = np.matmul(data, w).reshape((200, 1))

# 100 个训练数据
train_data = data[: 100]
train_label = label[: 100]

# 100 个验证数据
val_data = data[100: ]
val_label = label[100: ]

# 随机生成 w 训练参数
W1 = np.random.randn(input, hide_1) # (2, 5)
W2 = np.random.randn(hide_1, hide_2) # (5, 4)
W3 = np.random.randn(hide_2, output) # (4, 1)

# 学习率
lr = 1e-5


# 训练
def train_epoch(train_data, train_label, input, hide_1, hide_2, output, W1, W2, W3):
    for epoch in range(50000):
        # 前向传播
        # h0 层
        h0 = train_data.dot(W1) # (100, 2) * (2, 5) -> (100, 5)
        h0_relu = np.maximum(h0, 0)

        # h1 层
        h1 = h0_relu.dot(W2) # (100, 5) * (5, 4) -> (100, 4)
        h1_relu = np.maximum(h1, 0)

        # output 层
        y_pred = h1_relu.dot(W3)    # (100, 4) * (4, 1) -> (100, 1)

        # 损失函数
        loss = np.square(y_pred - train_label).sum()

        # 反向传播 求出 W1, W2, W3 的梯度
        # 输出层
        grad_y_pred = 2.0 * (y_pred - train_label)

        # h1 层
        grad_w3 = h1_relu.T.dot(grad_y_pred)
        grad_h1_relu = grad_y_pred.dot(W3.T)
        grad_h1 = grad_h1_relu.copy()
        grad_h1[h1 < 0] = 0

        # h0 层
        grad_w2 = h0_relu.T.dot(grad_h1)
        grad_h0_relu = grad_h1.dot(W2.T)
        grad_h0 = grad_h0_relu.copy()
        grad_h0[h0 < 0] = 0

        # 输入层
        grad_w1 = train_data.T.dot(grad_h0)

        # 更新模型参数 W
        W1 -= lr * grad_w1
        W2 -= lr * grad_w2
        W3 -= lr * grad_w3
        if epoch % 10000 == 0:
            print("train_loss", loss / 100)


train_epoch(train_data, train_label, input, hide_1, hide_2, output, W1, W2, W3)


# 验证
def val(val_data, input, hide_1, hide_2, output, W1, W2, W3):

    # h0 层
    h0 = val_data.dot(W1)
    h0_relu = np.maximum(h0, 0)

    # h1 层
    h1 = h0_relu.dot(W2)
    h1_relu = np.maximum(h1, 0)

    # 输出层
    y_val_pred = h1_relu.dot(W3)

    # 损失函数
    print("")
    return y_val_pred


y_val_pred = val(val_data, input, hide_1, hide_2, output, W1, W2, W3)

# 验证数据集预测和标签
fig = plt.figure(figsize=(10, 5))
y = []
y_val_label = []
for i in range(len(y_val_pred)):
    y.append(y_val_pred[i][0])
    y_val_label.append(val_label[i][0])

x = np.arange(0, 100)
plt.plot(x, y, 'ro-', x, y_val_label, 'bo-')
plt.show()

# 测试数据
test_data = np.array([[0.1, 0.5]])
y_test_pred = val(test_data, input, hide_1, hide_2, output, W1, W2, W3)
print(y_test_pred)