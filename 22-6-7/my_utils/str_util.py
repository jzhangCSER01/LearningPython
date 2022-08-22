"""
字符串相关工具
函数: str_reverse(s) 接收传入字符串 将字符串反转返回
函数: substr(s, x, y) 按照下标 x 和 y 对字符串进行切片
"""


def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s:   传入字符串
    :return:    反转后的字符串
    """
    return s[:: -1]


def substr(s, x, y):
    """
    按照下标 x 和 y 对字符串进行切片
    :param s:   传入字符串
    :param x:   开始下标
    :param y:   结束下标
    :return:    切片后的字符串
    """
    return s[x: y]


if __name__ == "__main__":
    print(str_reverse("abcde"))
    print(substr("abcde", 1, 4))