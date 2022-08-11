'''
单分支结构 检测用户是否正确输入用户名和密码
'''

a = dict((['mike', '001'], ['mary', '002'], ['john', '003'], ['tom', '004'], ['jenny', '005'], ['herry', '006']))
b = input('please input your name:')
c = input('please input your password:')
if(b in a) and c == a[b]:
    print('欢迎: %s' %b)