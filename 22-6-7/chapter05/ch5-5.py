"""
set 练习 信息去重
"""
# 定义列表对象
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast']
# 定义空集合
my_set = set()
# for 循环遍历列表
for element in my_list:
    # 将列表中的元素添加至集合
    my_set.add(element)
print(f"列表: {my_list}")
print(f"集合: {my_set}")