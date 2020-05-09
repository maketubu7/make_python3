# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 11:20
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : PRMD.py
# @Software: PyCharm

from sklearn.linear_model import LinearRegression
import numpy as np

def demo1():
    ''' 这种方式就是模拟线性回归，不能完全拟合曲线关系 '''
    x = np.random.uniform(-3,3,size=100)
    X = x.reshape(-1,1)
    y = 2.5*x**2 + 3 * x + 2 + np.random.normal(0,1,100)

    lir = LinearRegression()
    lir.fit(X,y)
    print(lir.coef_)

def demo2():
    '''模拟多项式回归，增加一个二次参数'''
    x = np.random.uniform(-3, 3, size=100)
    y = 2.5 * x ** 2 + 3 * x + np.random.normal(0, 1, 100)
    ## 增加参数
    X = x.reshape(-1, 1)
    x2 = np.hstack([X,X**2])
    lir = LinearRegression()
    lir.fit(x2, y)
    print(lir.coef_)
    print(lir.intercept_)
    print(x2[1:2,:])
    print(lir.predict(np.array([[1,1,],[2,4],])))

if __name__ == "__main__":
    demo2()