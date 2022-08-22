"""
tuple 常用功能练习
"""
t = ('周杰伦', 11, ['football', 'music'])
index = t.index(11)
print(f"年龄所在元组 t 中的下标是: {index}")
name = t[0]
print(f"学生的姓名是: {name}")

# 删除学生爱好中的 football
del t[2][0]
print(t)
# 增加爱好: coding 到爱好 list 内
t[2].append("coding")
print(t)