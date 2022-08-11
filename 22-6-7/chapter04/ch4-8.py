'''
Python 函数
可变数量的参数
Python 提供两种方法来处理可变数量的参数：非关键字可变数量参数和关键字可变数量参数。
1、非关键字可变数量参数（元组）
有非关键字可变数量参数时，函数头形式如下：def 函数名([标准化参数,]*非关键字可变数量参数):
'''

# 本例编写了具有非关键字可变数量参数的函数，演示非关键字可变数量参数如何定义和调用
def ftuple(arg1, arg2, arg3 = 333, *arg4):
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)
    print('arg3 = ', arg3)
    print('the rest args:')
    for ag in arg4:
        print(ag)
print(ftuple(1, 2, 3))
print(ftuple(1, 2))
print(ftuple(1, 2, 3, 4, 5, 6, 7))

'''
2、关键字可变数量参数（字典）
函数头形式如下：def 函数名([标准化参数,][*非关键字可变数量参数,] **关键字可变数量参数)
'''
print('------')
def fdict(arg1, arg2, arg3 = 333, **arg4):
    print('formal args:')
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)
    print('arg3 = ', arg3)
    print('the rest args:')
    for agkey in arg4:
        print(agkey, ':', arg4[agkey])
print(fdict(1, 2))
print(fdict(1, 2, 3))
print(fdict(1, 2, er = 3))