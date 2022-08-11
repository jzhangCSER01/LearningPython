'''
函数对象作参数如何定义与调用
'''

# 将序列中的每个元素加 2
def f(x):
    return x + 2
def ff(fun, seq):
    return [fun(eachn) for eachn in seq]
print(ff(f, [1, 2, 3, 4, 5, 6]))