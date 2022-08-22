"""
序列的切片
"""
str = "万过薪月，员序程马黑来，nohtyP学"

# 得到 "黑马程序员"
index1 = str.index("员")
index2 = str.index("黑")
new_str = str[index2 : index1 - 1 : -1]
print(f"切片后的序列为: {new_str}")