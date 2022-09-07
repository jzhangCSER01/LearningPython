"""
常用损失函数
"""


import torch

# 1. L1LOSS
# CLASS torch.nn.L1Loss(reduction='mean')
loss = torch.nn.L1Loss()
input = torch.randn(2, 2, requires_grad=True)   # torch.randn() 标准正太分布
target = torch.randn(2, 2)
output = loss(input, target)
print(input)
print(target)
print(output)


# 2. CrossEntropyLoss(交叉熵损失函数)
# CLASS torch.nn.CrossEntropyLoss(weight=None, ignore_index=-100, reduction='mean')
# CrossEntropyLoss = softmax + NLLLoss
loss = torch.nn.CrossEntropyLoss()
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
output = loss(input, target)
output.backward()
print(input)
print(target)
print(output)


# 3. NLLLoss(最大似然损失函数)
# CLASS torch.nn.NLLLoss(weight=None, ignore_index=-100, reduction='mean')
m = torch.nn.LogSoftmax(dim=1)
loss = torch.nn.NLLLoss()
# input is of size N x C = 3 x 5
input = torch.randn(3, 5, requires_grad=True)
# each element in target has to have 0 <= value < C
target = torch.tensor([1, 0, 4])
output = loss(m(input), target)
output.backward()
print(m(input))
print(target)
print(output)


# 4. MSELoss(平方损失函数)
# CLASS torch.nn.MSELoss(reduction='mean')
loss = torch.nn.MSELoss()
input = torch.randn(2, 2).floor()
target = torch.randn(2, 2).floor()
output = loss(input, target)
print(input)
print(target)
print(output)


# 5. DiceLoss(用于计算两个样本点的相似度的距，主要应用，语义分割等)
def dice_loss(input, target):
    input = input.contiguous().view(input.size()[0], -1)
    target = target.contiguous().view(target.size()[0], -1).float()
    a = torch.sum(input * target, 1)           # |X⋂Y|
    b = torch.sum(input * input, 1) + 0.001    # |X|
    c = torch.sum(target * target, 1) + 0.001  # |Y|
    d = (2 * a) / (b + c)
    return 1-d
input = torch.randn(2, 2).floor()
target = torch.randn(2, 2).floor()
output = dice_loss(input, target)
print(input)
print(target)
print(output)