'''
内建函数 map、filter、reduce
1、map 函数
map 函数的使用格式为：map(函数或 lambda 表达式,序列 1[,序列 2……])
将函数或 lambda 表达式作用于给定序列的每一个元素，并用一个列表来提供返回值，如果调用时给定了多个序列，则 map 会并行迭代每个序列。
每次处理时，map 会将每个序列的相应元素组成一个元组，然后将函数或 lambda 表达式作用于该元组。
'''

a = []
for e in map(lambda x : x * x, [2, 6, 4, 8]):
    a.append(e)
print(a)

'''
有时 map 函数可以被列表解析取代
例如：
>>>map(lambda x:x*x,[2,6,4,8])
等价于：
>>>[x*x for x  in [2,6,4,8]]
如果 map 函数中的函数名或 lambda 表达式为 None，则返回一个列表，列表的每个元素为一个元组，由各个序列相应元素组成，其功能类似内建函数 zip
'''
a = list(zip([1, 2, 3, 4], [5, 6, 7, 8, 9], [11, 22, 33, 44, 55, 66]))
print(a)
b = map([1, 2, 3, 4], [5, 6, 7, 8, 9], [11, 22, 33, 44, 55, 66])
print(b)

'''
2、filter 函数
filter 函数的使用格式为：filter(函数或 lambda 表达式,序列)
功能：利用函数或 lambda 表达式对序列中的每个元素进行筛选，保留函数值为 True 的元素序列。
'''

# 筛选出序列中的奇数
def odd(n):
    if(n % 2):
        return True
print(list(filter(odd, [1, 2, 3, 4, 5, 6])))

'''
3、reduce 函数
reduce 函数的使用格式为：reduce(函数或 lambda 表达式,序列[,初始值])
功能：函数或 lambda 表达式必须是二元函数（两个操作数），如果有初始值，则先把初始值和序列的第一个元素作为函数参数，求得返回值后，
再将返回值和序列的第二个元素作为函数参数，依此类推，直至序列最后一个元素。如果省略初始值，则先把序列的第一个和第二个元素作为函数参数，求得返回值后，
再将返回值和序列的第三个元素作为函数参数，依此类推，直至序列最后一个元素。
注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数
'''

from functools import reduce
print(reduce(lambda x, y : x * y, [1, 2, 3, 4, 5, 6], 10))