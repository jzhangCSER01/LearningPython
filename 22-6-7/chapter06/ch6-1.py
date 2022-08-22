"""
file 练习 单词计数
"""
with open("D:/PythonCode/PycharmProjects/LearningPython/22-6-7/chapter06/word.txt", 'r', encoding='UTF-8') as f:
    count = 0
    for line in f:
        for s in str(line).replace("\n", '').split(" "):
            if "itheima" == s:
                count += 1
print(f"itheima 的个数为: {count}")