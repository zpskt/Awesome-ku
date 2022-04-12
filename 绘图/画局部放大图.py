'''
局部放大图
'''
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np

def zone_and_linked(ax, axins, zone_left, zone_right, x, y, linked='bottom',
                    x_ratio=0.1, y_ratio=0.1):
    """缩放内嵌图形，并且进行连线
    ax:         调用plt.subplots返回的画布。例如： fig,ax = plt.subplots(1,1)
    axins:      内嵌图的画布。 例如 axins = ax.inset_axes((0.4,0.1,0.4,0.3))
    zone_left:  要放大区域的横坐标左端点
    zone_right: 要放大区域的横坐标右端点
    x:          X轴标签
    y:          列表，所有y值
    linked:     进行连线的位置，{'bottom','top','left','right'}
    x_ratio:    X轴缩放比例
    y_ratio:    Y轴缩放比例
    """
    xlim_left = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
    xlim_right = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio





    y_data = np.hstack([yi[zone_left:zone_right] for yi in y])
    ylim_bottom = np.min(y_data) - (np.max(y_data) - np.min(y_data)) * y_ratio
    ylim_top = np.max(y_data) + (np.max(y_data) - np.min(y_data)) * y_ratio

    axins.set_xlim(xlim_left, xlim_right)
    axins.set_ylim(ylim_bottom, ylim_top)

    ax.plot([xlim_left, xlim_right, xlim_right, xlim_left, xlim_left],
            [ylim_bottom, ylim_bottom, ylim_top, ylim_top, ylim_bottom], "black")

    if linked == 'bottom':
        xyA_1, xyB_1 = (xlim_left, ylim_top), (xlim_left, ylim_bottom)
        xyA_2, xyB_2 = (xlim_right, ylim_top), (xlim_right, ylim_bottom)
    elif linked == 'top':
        xyA_1, xyB_1 = (xlim_left, ylim_bottom), (xlim_left, ylim_top)
        xyA_2, xyB_2 = (xlim_right, ylim_bottom), (xlim_right, ylim_top)
    elif linked == 'left':
        xyA_1, xyB_1 = (xlim_right, ylim_top), (xlim_left, ylim_top)
        xyA_2, xyB_2 = (xlim_right, ylim_bottom), (xlim_left, ylim_bottom)
    elif linked == 'right':
        xyA_1, xyB_1 = (xlim_left, ylim_top), (xlim_right, ylim_top)
        xyA_2, xyB_2 = (xlim_left, ylim_bottom), (xlim_right, ylim_bottom)

    con = ConnectionPatch(xyA=xyA_1, xyB=xyB_1, coordsA="data",
                          coordsB="data", axesA=axins, axesB=ax)
    axins.add_artist(con)
    con = ConnectionPatch(xyA=xyA_2, xyB=xyB_2, coordsA="data",
                          coordsB="data", axesA=axins, axesB=ax)
    axins.add_artist(con)



#数据处理
def handleData(data):
    '''
    对数据进行处理
    :param data: 输入list的str数据
    :return: list的float数据
    '''
    for i in range(len(data)):
        data[i] = float(data[i].strip("%"))
    return data
#三个准确率对比图
data = pd.read_csv("./data/attack-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
x = data[0,1:]
ly1 = data[1,1:]
ly2 = data[2,1:]
ly3 = data[3,1:]
y1 = handleData(data[1,1:])#获取第一行的，所有列数 syft
y2 = handleData(data[2,1:])# Fate
y3 = handleData(data[3,1:])# PriChainFL


# x坐标
x = np.arange(0, 150)

# # 生成y轴数据，并添加随机波动
# y1 = np.log(x)
# indexs = np.random.randint(0, 1000, 800)
# for index in indexs:
#     y1[index] += np.random.rand() - 0.5
#
# y2 = np.log(x)
# indexs = np.random.randint(0, 1000, 800)
# for index in indexs:
#     y2[index] += np.random.rand() - 0.5
#
# y3 = np.log(x)
# indexs = np.random.randint(0, 1000, 800)
# for index in indexs:
#     y3[index] += np.random.rand() - 0.5

# 绘制主图
fig, ax = plt.subplots(1,1,figsize=(12,7))
#设置横纵坐标
plt.xlabel('Aggregation rounds')
plt.ylabel('Accuracy')
plt.title("Accuracy Comparison ")

ax.plot(x,y1,color='#f0bc94',label='PySyft',alpha=1.0, linewidth=2.0)
ax.plot(x,y2,color='#7fe2b3',label='FATE',alpha=1.0, linewidth=2.0)
ax.plot(x,y3,color='#cba0e6',label='PriChainFL',alpha=1.0, linewidth=2.0)
ax.legend(loc='right')

# plt.show()
#把坐标加个%号
def to_percent(temp, position):
    return '%1.0f' % (1 * temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
# 绘制缩放图
axins = ax.inset_axes((0.4, 0.1, 0.4, 0.3))

# 在缩放图中也绘制主图所有内容，然后根据限制横纵坐标来达成局部显示的目的
axins.plot(x,y1,color='#f0bc94',label='PySyft',alpha=1)
axins.plot(x,y2,color='#7fe2b3',label='FATE',alpha=1)
axins.plot(x,y3,color='#cba0e6',label='PriChainFL',alpha=1)

# 局部显示并且进行连线
zone_and_linked(ax, axins, 55, 73, x, [ly1,ly2,ly3], 'right')

#设置网格线
plt.grid(True) #显示网格线
plt.savefig("../Result/attack-Accuracy.png", dpi=300, bbox_inches='tight')
plt.show()

