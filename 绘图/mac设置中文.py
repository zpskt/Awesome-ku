import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"/System/Library/Fonts/STHeiti Medium.ttc", size=15)
print (matplotlib.matplotlib_fname()) # 将会获得matplotlib配置文件
x = np.linspace(-3, 3, 100)
y1 = 2 * x + 1
y2 = x ** 2

# 坐标轴范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 横纵坐标描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

l1, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
l2, = plt.plot(x, y2, color='blue', linewidth=5.0, linestyle='-')

# 图例
plt.legend(handles=[l1, l2], labels=['test1', 'test2'], loc='best')

plt.show()
x = np.linspace(0, 200, 1000)
y1 = 200 - 2 * x
y2 = x ** 0.5

# xy范围
plt.xlim((0, 200))
plt.ylim((0, 200))

# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# xy描述
plt.xlabel('情节数')
plt.ylabel('迭代次数')

l1, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
l2, = plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='-')

# 画图例
plt.legend(handles=[l1, l2], labels=['IRL', 'GAN-IRL'])  # ,loc='right'

plt.show()