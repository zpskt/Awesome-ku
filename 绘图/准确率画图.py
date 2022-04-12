#读取数据
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#数据处理
def handleData(data):
    '''
    对数据进行处理，去掉%号
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

#PriChainFL数据
data = pd.read_csv("PriChainFL-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
pri_x = data[0,1:]
pri_alice = handleData(data[1,1:])#获取第一行的，所有列数
pri_bob = handleData(data[2,1:])
pri_charlie=handleData(data[3,1:])
pri_FL=handleData(data[4,1:])
#Fate数据
data = pd.read_csv("Fate-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
fate_x = data[0,1:]
fate_alice = handleData(data[1,1:])#获取第一行的，所有列数
fate_bob = handleData(data[2,1:])
fate_charlie=handleData(data[3,1:])
fate_FL=handleData(data[4,1:])

#三个准确率对比图
data = pd.read_csv("3-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组
comp_rounds = data[0,1:]
comp_syft = handleData(data[1,1:])#获取第一行的，所有列数
comp_prichainFL=handleData(data[2,1:])
comp_fate = handleData(data[3,1:])
#绘图
def drawCompareAccuracy():
    # # 坐标轴范围
    # plt.xlim((0, 155))
    # plt.ylim((0, 1))
    # 横纵坐标描述
    plt.xlabel('Aggregation rounds')
    plt.ylabel('Accuracy')
    plt.title("Accuracy Comparison ")
    l1, = plt.plot(comp_rounds, comp_syft, color='red', linewidth=2.0, linestyle='-')
    l2, = plt.plot(comp_rounds, comp_fate, color='green', linewidth=2.0, linestyle='-')
    l3, = plt.plot(comp_rounds, comp_prichainFL, color='blue', linewidth=2.0, linestyle='-')

    plt.xticks(np.linspace(0,150,10,endpoint=True))#设置横坐标间隔
    plt.yticks(np.linspace(0,100,5,endpoint=True))#设置纵坐标间隔

    # 图例
    plt.legend(handles=[l1,l2,l3], labels=['PySyft','FATE','PriChainFL'], loc='best')
    #把坐标加个%号
    def to_percent(temp, position):
        return '%1.0f' % (1 * temp) + '%'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    # plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
    #设置网格线
    plt.grid(True) #显示网格线
    #保存图像 dpi设置清晰度
    plt.savefig("../Result/comparison-Accuracy.png",dpi=300,bbox_inches = 'tight')
    plt.show()
    #
def drawAccuracy(rounds,alice,bob,charlie,FL,picName):
    # # 坐标轴范围
    # plt.xlim((0, 155))
    # plt.ylim((0, 1))
    # 横纵坐标描述
    plt.xlabel('Aggregation rounds')
    plt.ylabel('Accuracy')
    plt.title(picName+" Accuracy")
    l1, = plt.plot(rounds, alice, color='red', linewidth=2.0, linestyle='-')
    l2, = plt.plot(rounds, bob, color='green', linewidth=2.0, linestyle='-')
    l3, = plt.plot(rounds, charlie, color='brown', linewidth=2.0, linestyle='-')
    l4, = plt.plot(rounds, FL, color='blue', linewidth=2.0, linestyle='-')


    plt.xticks(np.linspace(0, 150, 10, endpoint=True))  # 设置横坐标间隔
    plt.yticks(np.linspace(0, 100, 5, endpoint=True))  # 设置纵坐标间隔

    # 图例
    plt.legend(handles=[l1, l2, l3,l4], labels=['alice', 'bob', 'charlie',picName], loc='best')

    # 把坐标加个%号
    def to_percent(temp, position):
        return '%1.0f' % (1 * temp) + '%'

    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    # plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
    # 设置网格线
    plt.grid(True)  # 显示网格线
    # 保存图像 dpi设置清晰度
    plt.savefig("../Result/"+picName+"-Accuracy.png", dpi=300, bbox_inches='tight')
    plt.show()

drawCompareAccuracy()
drawAccuracy(pri_x,pri_alice,pri_bob,pri_charlie,pri_FL,"PriChainFL")
drawAccuracy(syft_x,syft_alice,syft_bob,syft_charlie,syft_FL,"PySyft")
drawAccuracy(fate_x,fate_alice,fate_bob,fate_charlie,fate_FL,"FATE")
