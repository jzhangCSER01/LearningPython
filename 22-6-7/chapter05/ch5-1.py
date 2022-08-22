"""
list 常用功能练习
"""

# 定义列表 myList
myList = [21, 25, 21, 23, 22, 20]
# 追加一个数字 31 到列表的尾部
myList.append(31)
# 追加一个新列表 [29, 33, 30] 到列表的尾部
myList.extend([29, 33, 30])
# 取出第一个元素 21
first = myList[0]
# 取出最后一个元素 30
last = myList[-1]
# 查找元素 31 在列表中的下标位置
index = myList.index(31)
print(index)