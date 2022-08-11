radius = input(u"输入半径：")
radius_float = float(radius)
area = radius_float**2*3.1415926
print(u'面积：' + str(area))

'''
a = 3.14
print(a.__sizeof__())

Python的浮点数实现原理：
CPython实现有⼀个PyFloatObject的结构体，用来构造Python的浮点数类型：
typedef struct {
PyObject_HEAD # 这个对象包含：引用计数+对象类型，占8+8=16字节
double ob_fval; # 这个是存储浮点数的地方，Python的浮点数就是C的double，即双精度浮点
} PyFloatObject;
所以Python的浮点数类型占24字节
'''

'''
from decimal import *
x = Decimal('0.3')
y = x / Decimal(3)
print(y)

十进制浮点型 Decimal 精度更高，使用 decimal.Decimal() 来存储精确的数字
'''

'''
复数 Complex
x + yj, x 是实数部分，y 是虚数部分
（1）复数由实数部分和虚数部分构成。
（2）表示复数的语法是：real+imgj。
（3）虚部不能单独存在，它们总是和一个值为 0.0 的实部一起构成一个复数。
（4）实数部分和虚数部分都是浮点数。
（5）虚数部分必须有后缀 j 或 J。
复数对象拥有重要的数据属性 real 和 imag，分别表示该复数的实部和虚部。
Python 为复数类型提供了 conjugate 方法，调用它可以返回复数的共轭复数对象。
'''

'''
算数运算符
** 幂运算 (8**3 = 8的3次方 = 512)
/ 除法运算，若两个操作数都是整数则除为“地板除”，否则为真正除。在 Python3.x 中，运算符/对应着真正的除法，即 1/2=0.5
// “地板除”(floor)是指取比商小的最大整数，如 5//2=2，-5//2=-3。
幂运算符比其左侧操作数的一元运算符优先级低，比其右侧操作数的一元运算符的优先级高
-2**3  #相当于 -(2**3)
2**-3  #相当于 2**(-3)
函数 divmod()把除和求余运算结合起来，返回一个包含商和余数的元组。divmod(n1,n2) 的结果为 (n1//n2，n1%n2)
'''