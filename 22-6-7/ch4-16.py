'''
global 语句
如果想在函数中改变全局变量的值，需要先在函数体中用 global 对全局变量进行声明。
'''

g_x = 2345  # 全局变量
def fun():
    global g_x
    g_x = 6789
    print('函数内 g_x', g_x)
print('调用函数前，函数外 g_x = ', g_x)
fun()
print('调用函数后，函数外 g_x = ', g_x)