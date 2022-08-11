'''
Python 函数
def 函数名(参数):
    文档字符串（可以省略，但推荐编写，便于日后维护和理解）
    函数体
    return 返回值 （可以省略，如省略，Python 解释器会返回 None）
'''

def myprint():
    '''
    print hello world
    :return:
    '''
    print('hello world')
myprint()
print(myprint.__doc__)