"""
测试使用自定义 包 模块
"""
import sys
sys.path.append(r"D:/PythonCode/PycharmProjects/LearningPython/22-6-7/")
import my_utils.str_util
print(my_utils.str_util.str_reverse("黑马程序员"))
from my_utils import file_util as fu
fu.print_file_info("D:/PythonCode/PycharmProjects/LearningPython/22-6-7/chapter06/word.txt")