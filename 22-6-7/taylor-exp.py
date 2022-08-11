'''
Taylor 公式的应用: 求 exp(x)
'''
import math
import numpy as np
from matplotlib import pyplot as plt

'''
x 较小时，近似估计 e^x 的值
'''
def cal_e_small(x):
    n = 10
    denominator = np.arange(1, n + 1).cumprod() # 分母
    numerator = np.array([x] * n).cumprod() # 分子
    return np.sum(numerator / denominator) + 1

'''
令 x = k * ln2 + r, |r| ≤ 0.5 * ln2
从而 e^x = 2^k * e^r
'''
def cal_e(x):
    reverse = False
    if x < 0:
        x = -x
        reverse = True
    ln2 = 0.69314718055994530941723212145818
    '''
    因为 |r| <= ln2 / 2
    所以 x - k * ln2 <= ln2 / 2
    k * ln2 >= x - ln2 / 2
    k >= x / ln2 - 0.5
    因为 k 是整数
    '''
    c = x / ln2
    k = int(c + 0.5)
    r = x - k * ln2
    y = (2 ** k) * cal_e_small(r)
    if reverse:
        return 1 / y    # e^-x = 1 / e^x
    return y

'''
main 函数
'''
if __name__ == "__main__":
    t1 = np.linspace(-2, 0, 10, endpoint=False)
    t2 = np.linspace(0, 2, 20)
    t = np.concatenate((t1, t2))    # numpy.concatenate((a1,a2,...), axis=0)函数。能够一次完成多个数组的拼接。其中a1,a2,...是数组类型的参数
    print(t)    # 横轴数据
    y = np.empty_like(t)    # 未初始化(任意)数据的数组，其形状和类型与原型相同
    for i, x in enumerate(t):
        y[i] = cal_e(x)
        print('e^', x, ' = ', y[i], '(近似值)\t', math.exp(x), '(真实值)')
        print('误差', y[i] - math.exp(x))
    plt.rcParams['font.sans-serif'] = [u'SimHei']   # 显示中文
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(t, y, 'r-', t, y, 'go', linewidth=2)
    plt.title('Taylor 公式的应用', fontsize=18)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('exp(x)', fontsize=15)
    plt.grid(True)
    plt.show()
