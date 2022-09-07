"""
参数初始化
"""


import torch
from torch import nn

net = nn.Sequential(nn.Linear(4, 5), nn.ReLU(), nn.Linear(5, 1))


def init_normal(m):
    if type(m) == nn.Linear:
        # 方法一 均值为0，方差为0.01 的高斯分布
        nn.init.normal_(m.weight, mean=0, std=0.01)
        # 方法二 常数初始化
        # nn.init.constant_(m.weight, 1)
        # 方法三  Xavier初始化
        # nn.init.xavier_uniform_(m.weight)
        # 方法四 自定义初始化 -1 到 1 均匀分布
        # nn.init.uniform_(m.weight, -1, 1)
        nn.init.zeros_(m.bias)


net.apply(init_normal)
X = torch.randn(2, 4)
output = net(X)
print(output)
print(net)
print(net[0].weight)
print(net[2].weight)
# net[0].apply(init_normal)   # 也可以只更新第一层参数