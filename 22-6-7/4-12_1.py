'''
Python 装饰器
https://zhuanlan.zhihu.com/p/87353829
'''

# 无参数装饰器
import time
# 定义一个计时器函数，其参数为一个函数，用于接收被装饰的函数
def time_stt(func):
    # 定义一个内嵌的包装函数，记录函数开始时间和结束时间
    def wrapper(*t, **d):
        start = time.time()
        func(*t, **d)
        usetime = time.time() - start
        print('执行函数', func.__name__, '用时', usetime, '秒')
    return wrapper  # 返回包装后的函数

@time_stt
def test():
    time.sleep(4)
print('装饰无参数的函数试验:')
test()

@time_stt
def pr(n):
    for i in range(n):
        print(i)
print('装饰一个参数函数试验:')
pr(4)

@time_stt
def area(l, w):
    print('面积为:', l * w)
print('装饰两个参数函数试验:')
area(40, 23)