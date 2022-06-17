'''
for 循环
for 语句的使用格式：
for 迭代变量 in 迭代对象:
    循环体
迭代对象可以是序列、迭代器或其他支持迭代的对象
'''

namelist = ('古巨基', '孙楠', '黄丽玲', '胡彦斌', '陈洁仪', '张靓颖', '韩红')
# n = 1
for n, sn in enumerate(namelist):
    print('第', n + 1, '位出场歌手: ', sn)

'''
range 函数的使用格式: range(初值, 终值, 步长)
range 函数会返回一个包含“（终值-初值）/步长”个元素的有序列表，各元素的值大于
或等于初值且小于终值，range 函数的三个参数（初值,终值,步长）都要求是整型数字，步长
省略则默认为 1，初值省略则默认为 0
'''

s = 0
for n in range(1, 101):
    s = s + n
print('1 + 2 + 3 + … + 100 = ', s)

'''
xrange 函数与 range 函数类似，但不会在内存中创建列表的完整副本。它只能用于 for循环中，在 for 循环外，xrange 函数毫无意义。
xrange(初值,终值,步长)
'''

# 字典迭代器
teldict = {'mary' : '1362456737', 'john' : '13609822567', 'tom' : '15920488245'}
for (name, tel) in teldict.items():
    print(name, ':', tel)