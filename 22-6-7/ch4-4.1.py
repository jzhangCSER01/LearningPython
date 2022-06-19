'''
函数式编程
1、lambda 表达式
Python 允许用关键字 lambda 创建匿名函数。创建格式如下：
lambda[参数 1[,参数 2[……[,参数 N]]]:表达式
说明：
（1）lambda 中的表达式必须与声明放在同一行。
（2）lambda 的参数是可选的，参数不需加括号。
'''

# 求矩形面积的函数改写成 lamda 创建的匿名函数
'''
lambda L, W : L * W
为了保留并调用这个函数，可以将这个匿名函数赋给一个变量，通过变量来调用函数，也可以将匿名函数用作函数参数，通过函数参数来调用
'''
# 赋值给变量:
y = lambda L, W : L * W
print(y(3, 4))

# 用作函数参数: 首先定义一个使用函数参数的函数
def area(func, seq1):
    seq = []
    for (x, y) in seq1:
        seq.append(func(x, y))
    return seq
# 调用时使用 lambda 语句创建的匿名函数作实参
print(area(lambda L, W : L * W, [(1, 2), (3, 4), (5, 6)]))