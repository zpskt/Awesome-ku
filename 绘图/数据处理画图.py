#读取数据
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter
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
#syft数据
data = pd.read_csv("./data/Syft-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
syft_x = (data[0,1:])
syft_alice = handleData(data[1,1:])#获取第一行的，所有列数
syft_bob = handleData(data[2,1:])
syft_charlie=handleData(data[3,1:])
syft_FL=handleData(data[4,1:])


#绘图
import matplotlib.pyplot as plt
import numpy as np
# # 坐标轴范围
# plt.xlim((0, 155))
# plt.ylim((0, 1))
# 横纵坐标描述
plt.xlabel('Aggregation rounds')
plt.ylabel('Accuracy')
plt.title("Accuracy Comparison ")

l1, = plt.plot(syft_x, syft_alice, color='red', linewidth=1.0, linestyle='-')
l2, = plt.plot(syft_x, syft_bob, color='green', linewidth=1.0, linestyle='-')
l3, = plt.plot(syft_x, syft_charlie, color='brown', linewidth=1.0, linestyle='-')
l4, = plt.plot(syft_x, syft_FL, color='blue', linewidth=1.0, linestyle='-')

plt.xticks(np.linspace(0,150,9,endpoint=True))#设置横坐标间隔
plt.yticks(np.linspace(0,100,5,endpoint=True))#设置纵坐标间隔

# 图例
plt.legend(handles=[l1,l2,l3,l4], labels=['alice','bob','charlie', 'PySyft'], loc='best')

def to_percent(temp, position):
    '''
    把0-100转换成0%-100%，可以设置变成%号后大小
    :param temp:
    :param position:
    :return:
    '''
    return '%1.0f' % (1 * temp) + '%'

plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.grid(True) #显示网格线
plt.show()
