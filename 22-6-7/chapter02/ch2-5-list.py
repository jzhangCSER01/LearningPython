'''
Python 列表实现向量加法
'''
# Python list
import time
t0 = time.perf_counter()    # Python 3.8中不支持clock()属性
a = range(100)  # 创建一个有100个元素的列表，取值0-99
b = []
c = []
for i in range(100):
    b.append(a[i] * a[i])
    c.append(a[i] + b[i])
print(c)
print(time.perf_counter() - t0)