y = '''yueoeo
jeekrk
elerk'''
print(y)
s = 'hello\nworld'
print(s)

'''
Python 中有三类字符串：通常意义字符串、原始字符串和 Unicode 字符串。
通常意义字符串即用单引号、双引号和三引号界定的文本
原始字符串是以 R 或 r 开始的字符串，不对其中的转义字符进行转义。在原始字符串中，所有的字
符都是直接按照字面的意思来使用，即没有转义和不能打印的字符。
Unicode 是书写国际文本的标准方法，如果文件中含有非英语文本，就必须使用 Unicode 字符串。Unicode 字符串是以 U 或 u 开始的字符串
'''

x = 'have a nice day'
print(x[0: 10: 2])

'''
格式化字符串(%)
Python 的字符串格式化分为两种，一种是“%”形式类似 C 语言的 printf 函数，另外一种是 C#形式的“{0}.format”形式。
格式化操作符的使用格式为：格式化模板 % 转换参数列表
Python 中内置的%操作符可用于格式化字符串操作，控制字符串的呈现格式。
'''

print('%i'%23)
print('%u'%3456)

'''
字符串内建函数
1、字符串去空格(strip, lstrip, rstrip)
strip 去掉字符串左侧和右侧的空格（包括空格键、Tab 键和回车键），lstrip 去掉字符串左侧的空格，rstrip 去掉字符串右侧的空格。
如果在 strip、lstrip、rstrip 函数的参数中给出特定字符串，这三个函数也可以完成删除特殊字符的功能。
2、连接字符串(join)
除了使用操作符“+”实现字符串连接功能，也可以使用 join 函数连接字符串
3、分割和组合(split, rsplit, splitlines)
split 函数的使用格式为：string.split(str,num) 功能：以 str 为分隔符切片 string，如果指定 num，则仅分割 num 个子字符串。
rsplit 函数与 split 基本相同，区别在于当 num<string.count(str)时，split 是从左向右分割子字符串，而 rsplit 是从右向左分割子字符串。
splitlines 函数的使用格式为：string.splitlines(num) 功能：按照行切片 string，返回一个以各行内容为元素的列表，如果指定 num，则仅切片 num 行。
4、查找字符串(find、index)
find 函数的使用格式为：string.find(str,beg,end)
功能：检测 str 是否包含在 string 中，如果用 beg 和 end 指定范围，则会检查是否包含在指定范围内，如果是，返回开始的索引值，否则返回-1。
index 函数的使用格式为：string.index(str,beg,end)
功能：与 find 函数基本相同，只是如果在 string 中找不到 str 会报告异常。
5、统计子字符串出现次数(count)
count 函数的使用格式为：string.count(str,beg,end)
功能：统计 str 在 string 中的出现次数，如果用 beg 和 end 指定范围，则返回指定范围内 str 出现的次数。
6、替换子字符串(replace)
replace 函数的使用格式为：string.replace(str1,str2,num)
功能：把字符串中的字符串 str1 替换成 str2，如果 num 指定，则替换次数不超过 num 次。
7、字符串的测试、判断函数
string.startswith(str[,beg[,end]]) 检查是否以 str 开头，如果指定 beg 和 end，则在指定范围内查找。
string.endswith(str[,beg[,end]]) 检查是否以 str 结尾，如果指定 beg 和 end，则在指定范围内查找。
string.isalnum()检查是否全是字母和数字，并至少有一个字符。
string.isalpha()检查是否全是字母，并至少有一个字符。
string.isdigit()检查是否全是数字，并至少有一个字符。
string.isspace()检查是否全是空白字符，并至少有一个字符。
string.islower()检查是否全是小写。
string.isupper()检查是否全是大写。
string.istitle()检查是否首字母大写。
可使用 capitalize 函数将字符串的首字符改成大写
'''

c = ''.join(('ab', 'cd', 'ef'))
print(c)
b = 'I am \na student'
print(b)
print(b.splitlines())