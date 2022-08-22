"""
成年人判断
"""
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print("您已成年，游玩需要补票 10 元。")
# else:
#     print("祝您游玩愉快。")
number = 6
if int(input("请输入第一次猜想的数字: ")) == number:
    print("猜对了1")
elif int(input("不对，再猜一次: ")) == number:
    print("猜对了2")
elif int(input("不对，再猜最后一次: ")) == number:
    print("猜对了3")
else:
    print(f"Sorry, 猜错了，我想的是: {number}")
