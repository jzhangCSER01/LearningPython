'''
求一个数的最大真因数
'''

n = int(input('please input the number:'))
m = n // 2   # 一个数的最大真因数不可能大于其值一半
while(m > 0):
    if(n % m == 0):
        print(n, '的最大真因数是：', m)
        break
    m = m - 1