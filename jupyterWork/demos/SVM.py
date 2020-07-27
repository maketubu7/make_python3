# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 11:47
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : SVM.py
# @Software: PyCharm
# @describe: 支撑向量机和高斯核函数

from sklearn.svm import LinearSVC,SVC
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def linearSVC_demo():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X = X[y < 2, :2]
    y = y[y < 2]
    linearsvc = plotminiSVC(1)
    linearsvc.fit(X,y)
    return linearsvc


def plotminiSVC(C=1,gamma=1):
    return Pipeline(
        [("std_scaler", StandardScaler()),
         ("linearSVC", LinearSVC(C=C))]
    )


def plotmultiSVC(C=1,gamma=1):
    return Pipeline(
        [("std_scaler", StandardScaler()),
         ("linearSVC", SVC(C=C,gamma=gamma))]
    )


def guuasK_function():

    def gamma(x,l):
        gamma = 1.0
        return np.exp(-gamma* (x-l)**2)

    X = np.arange(-4,5,1)
    y = np.array((X>=-2) & (X<=2), dtype="int")
    plt.scatter(X[y == 0], [0] * len(X[y == 0]))
    plt.scatter(X[y == 1], [0] * len(X[y == 1]))
    plt.show()

    X_new = np.empty((len(X),2))
    for i, data in enumerate(X):
        X_new[i,0] = gamma(data,-1)
        X_new[i,1] = gamma(data,1)

    return X_new,y

def RBF_kernel_svc():
    X,y = make_moons(noise=0.15,random_state=666)
    svc_gamma10 = plotmultiSVC(gamma=10)
    svc_gamma10.fit(X,y)


if __name__ == "__main__":
    # X,y = guuasK_function()
    RBF_kernel_svc()
    # plt.scatter(X[y == 0, 0], X[y == 0, 1])
    # plt.scatter(X[y == 1, 0], X[y == 1, 1])
    # plt.show()