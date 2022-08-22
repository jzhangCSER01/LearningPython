"""
黑马 ATM 案例
"""
money = 5000000 # 全局变量 money 表示账户余额
name = None # 全局变量 name 表示账户姓名 需要输入

name = input("请输入姓名: ")

# 查询余额
def query(show_menu):
    if show_menu:
        print("------查询------")
    print(f"{name} 您好, 您的账户余额为: {money}")

# 存款
def save(money_num):
    global money
    money += money_num
    print("------存款------")
    print(f"{name} 您好，您存入{money_num}，存款成功")
    query(False)

# 取款
def load(money_num):
    global money
    print("------取款------")
    if money < money_num:
        print(f"余额不足，当前余额为: {money} 元")
    else:
        money -= money_num
        print(f"{name} 您好，取款成功")
    query(False)

# 主菜单
def main():
    print("欢迎来到黑马 ATM")
    print("------")
    print("查询余额请输入\t[1]:")
    print("存款请输入\t[2]:")
    print("取款请输入\t[3]:")
    print("退出请输入\t[4]:")
    return int(input("请输入要执行的操作: "))

while True:
    command = main()
    if command == 1:
        query(True)
        continue
    elif command == 2:
        save_money = int(input("请输入要存入的金额: "))
        save(save_money)
        continue
    elif command == 3:
        load_money = int(input("请输入的要取款的金额: "))
        load(load_money)
        continue
    else:
        print("退出程序了")
        break
