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
data = pd.read_csv("Syft-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
syft_x = (data[0,1:])
syft_alice = handleData(data[1,1:])#获取第一行的，所有列数
syft_bob = handleData(data[2,1:])
syft_charlie=handleData(data[3,1:])
syft_FL=handleData(data[4,1:])

#PriChainFL数据
data = pd.read_csv("PriChainFL-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
pri_x = data[0,1:]
pri_alice = handleData(data[1,1:])#获取第一行的，所有列数
pri_bob = handleData(data[2,1:])
pri_charlie=handleData(data[3,1:])
pri_FL=handleData(data[4,1:])

#绘图
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# # 坐标轴范围
# plt.xlim((0, 155))
# plt.ylim((0, 1))
# 横纵坐标描述
plt.xlabel('Aggregation rounds')
plt.ylabel('Accuracy')
plt.title("PySyft Accuracy")
l1, = plt.plot(syft_x, syft_alice, color='red', linewidth=1.0, linestyle='-')
l2, = plt.plot(syft_x, syft_bob, color='green', linewidth=1.0, linestyle='-')
l3, = plt.plot(syft_x, syft_charlie, color='brown', linewidth=1.0, linestyle='-')
l4, = plt.plot(syft_x, syft_FL, color='blue', linewidth=1.0, linestyle='-')

plt.xticks(np.linspace(0,150,10,endpoint=True))#设置横坐标间隔
plt.yticks(np.linspace(0,100,5,endpoint=True))#设置纵坐标间隔

# 图例
plt.legend(handles=[l1, l2,l3,l4], labels=['alice','bob','charlie', 'PySyft'], loc='best')
#把坐标加个%号
def to_percent(temp, position):
    return '%1.0f' % (1 * temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
#设置网格线
plt.grid(True) #显示网格线
#保存图像 dpi设置清晰度
plt.savefig("../Result/PySyft-Accuracy.png",dpi=500,bbox_inches = 'tight')
plt.show()
#
