'''
带参数装饰器
@装饰器函数(装饰参数)
def 被装饰函数(参数):
带参数的装饰器函数必须返回一个函数对象，该函数对象才是真正装饰函数的装饰器
'''

# 用装饰器记录函数开始调用的时间或结束的时间
import time
def decselect(sel):
    def startdec(func):
        def r(*t, **d):
            print('下面调用函数:', func.__name__, '开始调用时间为:', time.ctime())
            func(*t, **d)
        return r
    def enddec(func):
        def r(*t, **d):
            print('函数:', func.__name__, '于', time.ctime(), '调用结束')
        return r
    try:
        return {'start' : startdec, 'end' : enddec}[sel]
    except KeyError as e:
        raise ValueError(e)('必须是"start"或"end"')

@decselect('end')
def sp(seq):
    '''
    输出一个序列
    :param seq:
    :return:
    '''
    for n in seq:
        print(n)
sp([1, 2, 3, 4, 5, 6])