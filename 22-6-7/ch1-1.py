
import matplotlib.pyplot as plt #install package matplotlib
import matplotlib as mpl
#myfont = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')
# 加这个两句 可以显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot([-2, 2, 3, 4, 5], 'r', label = u'第一条曲线')   #颜色为红色的曲线
plt.plot([1, 2, 3, 8, 5], 'b', label = u'第二条曲线')    #颜色为蓝色
#plt.legend()的作用：在plt.plot() 定义后plt.legend() 会显示该 label 的内容，否则会报error: No handles with labels found to put in legend.
plt.legend()
plt.grid(True)  #显示网格
plt.axis([0, 5, -3, 9]) #坐标轴的最大值与最小值
plt.xlabel(u'X轴坐标')    # 坐标轴标签
plt.ylabel(u'Y轴坐标')
plt.title(u'matplotlib演示图')
plt.show()

'''
import matplotlib.pyplot as plt

a = [1, 2, 3, 4] # y 是 a的值，x是各个元素的索引
b = [5, 6, 7, 8]

plt.plot(a, b, 'r--', label = 'aa')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
plt.legend()    # 将样例显示出来
plt.plot()
plt.show()
# 测试一次
'''
