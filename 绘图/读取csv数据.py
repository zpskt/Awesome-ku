import pandas as pd
import numpy as np

data = pd.read_csv("./data/Syft-accuracy.csv", header=None)#读取数据
data = np.array(data)#转换成数组

print(data)
print(type(data))

alice_accuracy = data[1,1:]#获取第一行的，所有列数
bob_accuracy = data[2,1:]
charlie_accuracy=data[3,1:]
PriChainFL=data[4,1:]
print(alice_accuracy)
print(bob_accuracy)
print(PriChainFL)
print(type(PriChainFL[0]))
def handleData(data):
    '''
    对数据进行处理
    :param data: 输入list的str数据
    :return: list的float数据
    '''
    for i in range(len(data)):
        data[i] = float(data[i].strip("%"))
    print(data)
    print(type(data))
    return data
new = handleData(PriChainFL)


