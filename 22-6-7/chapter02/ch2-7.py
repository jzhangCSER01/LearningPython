'''
字典(dict)
字典(dict)是 Python 中的映射数据类型，使用大括号{}作为界定符，由键-值（key-Value）对构成，通常使用数字或字符串作键，而值可以是任意类型的 Python 对象。
字典根据键来存取对象，所以字典中的键必须是唯一的。
创建字典时，键-值之间用冒号分隔，键-值对之间用逗号分隔。
'''

d = dict(one = 1, two = 2)
print(d)
for key in d:
    print('%s = %s'%(key, d[key]))

'''
添加字典元素 为字典添加新的元素的格式如下：字典变量名[新键名] = 值
删除字典元素 可使用 del 或字典的 pop()方法来删除字典元素。删除字典元素时，必须指定要删除元素的键
清空字典 使用 clear()方法可以清空字典中所有元素
hash()
Python 中字典的键要求是可 hash 的即不可变的对象，在 Python 内部是通过字典 key 的
hash 值来对应内存中的 value 地址的，可以使用 hash()函数判断某个对象是否可以做一个字
典的键。如果对象是可 hash 的，函数返回值是整型，否则会产生错误或异常。
'''

# tel book example
telbook = {'mike' : '1238569', 'john' : '1534755', 'mary' : '1235345', 'henry' : '1452568'}
name = input('whose number do you want to get:')
num = telbook.get(name)
print('%s\'s number is %s ' %(name, num))