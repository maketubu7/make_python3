# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 14:16
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : LogReg.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt

def sigmoid(t):
    return 1 / (1 + np.exp(-t))

def plot_x_y(x,y,title):
    plt.plot(x,y,color='r')
    plt.title(title)
    plt.axis([0,10,0,5])
    plt.show()

class LogisticRegession():
    def __init__(self):
        pass

if __name__ == "__main__":
    x = np.linspace(-10,10,500)
    # y = sigmoid(x)
    y = -np.log(x)
    plot_x_y(x,y,'y=1')