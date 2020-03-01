# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 13:40
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : simple-linear-implement.py
# @Software: PyCharm
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets



def func():
    x = np.array([1., 2., 3., 4., 5.])
    y = np.array([1., 3., 2., 3., 5.])
    plt.scatter(x, y)
    plt.axis([0, 6, 0, 6])


    x_mean = np.mean(x)
    y_mean = np.mean(y)

    sum = 0
    d = 0

    for x_i, y_i in zip(x,y):
        sum += (x_i-x_mean)*(y_i-y_mean)
        d += (x_i-x_mean) **2

    a = sum / d
    b = y_mean - a*x_mean

    y_hat = a*x +b
    plt.scatter(x, y)
    plt.plot(x, y_hat, color='r')
    plt.axis([0, 6, 0, 6])
    plt.show()

def boston():
    boston = datasets.load_boston()
    print(boston.feature_name)


if __name__ == "__main__":
    boston()