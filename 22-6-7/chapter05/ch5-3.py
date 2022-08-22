"""
string 练习
"""
# 给定一个字符串: "itheima itcast boxuegu"
str = "itheima itcast boxuegu"
# 统计字符串有多少个 "it" 字符
num_it = str.count("it")
print(f"字符串 str 中有 {num_it} 个 'it'")
# 将字符串内的空格 全部替换为字符: "|"
new_str = str.replace(" ", "|")
print(f"替换后的字符串是: {new_str}")
# 按照 "|" 进行字符串分割 得到列表
list_str = new_str.split("|")
print(f"分割后得到的列表为: {list_str}")