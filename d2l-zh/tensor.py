"""
pytorch tensor 张量
"""


import torch

# 创建一个大小为(2, 3)的 tensor, 元素全为 1, 类型为 64 位浮点型
# h = torch.ones(2, 3, dtype=torch.double)
# print(h)
a = torch.tensor([1.0])
print(a)

j = torch.tensor([1, 2, 3])
k = torch.tensor([2, 3, 4])

# 加法1
print("Tensor 加法: ", j + k)