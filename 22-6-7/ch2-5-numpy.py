import time
import numpy as np  # 导入 NumPy 模块
t0 = time.perf_counter()
a = np.arange(100)
b = np.arange(100)**2
c = a + b
print(c)
print(time.perf_counter() - t0)