"""
可视化需求1: 折线图开发
"""


import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f_us = open("./linechartdata/美国.txt", 'r', encoding='UTF-8')
us_data = f_us.read()   # 读取美国数据的全部内容

f_jp = open("./linechartdata/日本.txt", 'r', encoding='UTF-8')
jp_data = f_jp.read()   # 日本的全部内容

f_in = open("./linechartdata/印度.txt", 'r', encoding='UTF-8')
in_data = f_in.read()   # 印度的全部内容

# 去掉不合 json 规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不合 json 规范的结尾
us_data = us_data[: -2]
jp_data = jp_data[: -2]
in_data = in_data[: -2]

# json 转换为 python 字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取 trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据 用于 x 轴 取2020年(到 314 下标结束)
us_x_data = us_trend_data['updateDate'][: 314]
jp_x_data = jp_trend_data['updateDate'][: 314]
in_x_data = in_trend_data['updateDate'][: 314]
print(us_x_data)

# 获取确认数据 用于 y 轴 取2020年(到 314 下标结束)
us_y_data = us_trend_data['list'][0]['data'][: 314]
jp_y_data = jp_trend_data['list'][0]['data'][: 314]
in_y_data = in_trend_data['list'][0]['data'][: 314]
print(us_y_data)

# 生成图表
line = Line()   # 构建折线图对象

# 添加 x 轴数据
line.add_xaxis(us_x_data)   # x 轴是公用的

# 添加 y 轴数据
line.add_yaxis("美国确诊人数" ,us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数" ,jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数" ,in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020 年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

# 调用 render 方法 生成图标
line.render()

# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()