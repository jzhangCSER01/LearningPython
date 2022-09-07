'''
FashionMNIST 数据集
'''

import torch
import torchvision
from torch.utils import data
from torchvision import transforms

# 通过ToTensor实例将图像数据从PIL类型变换成32位浮点数格式，
# 并除以255使得所有像素的数值均在0到1之间
trans = transforms.ToTensor()    # 将图片转换为 tensor
mnist_train = torchvision.datasets.FashionMNIST(
    root="D:/AIProjects/d2l-zh/pytorch/data/FashionMNIST/",
    train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(
    root="D:/AIProjects/d2l-zh/pytorch/data/FashionMNIST/",
    train=False, transform=trans, download=True)
print(type(mnist_train))
print(mnist_train.shape, mnist_test.shape)