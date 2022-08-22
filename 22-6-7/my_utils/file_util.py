"""
文件处理相关工具
函数: print_file_info(file_name) 接收传入文件的路径 打印文件的全部内容 如文件不存在则捕获异常 输出提示信息 通过 finally 关闭文件对象
函数: append_to_file(file_name, data) 接收文件路径以及传入数据 将数据追加写入到文件中
"""


def print_file_info(file_name):
    """
    打印文件内容
    :param file_name:   传入文件路径
    :return:    None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        for e in f.readlines():
            print(e.strip("\n"))
    except Exception as e:
        print(f"文件不存在或路径不存在 异常信息: {e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    将数据追加写入到文件中
    :param file_name: 传入文件路径
    :param data: 要追加的数据
    :return: None
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.write("\n")
    f.close()