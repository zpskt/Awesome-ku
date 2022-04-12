import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 100)
y=np.arange(-100,0)
plt.subplot(131)#设置画布为2行两列，当前画第1个
plt.plot(x, y)
plt.subplot(132)#设置画布为2行两列，当前画第2个
plt.plot(x, -x)
plt.subplot(133)#设置画布为2行两列，当前画第3个
plt.plot(x, x ** 3)
plt.show()

