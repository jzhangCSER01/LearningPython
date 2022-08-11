'''
元组与列表类似，也是一种容器类型，但两者有本质的区别：列表是可变的，而元组是不可变的。
Python 使用圆括号()作为元组的界定符
'''

y = tuple('hello')
z = tuple('world')
print(y == z)