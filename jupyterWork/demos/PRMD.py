# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 11:20
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : PRMD.py
# @Software: PyCharm

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import numpy as np
import random
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error


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
    print(lir.predict(np.array([[1,1],[2,4]])))

def sk_demo():
    x = np.random.uniform(-3, 3, size=100)
    X = x.reshape(-1, 1)
    y = 2.5 * x ** 2 + 3 * x + 2 + np.random.normal(0, 1, 100)
    poly = PolynomialFeatures(degree=2)  ## 需要增加最多几次幂的特征
    poly.fit(X)
    ## 转换后的x的特征值
    X2 = poly.transform(X)

    lir = LinearRegression()
    # 对x转换后的特征值，进行训练
    lir.fit(X2,y)
    print(lir.coef_)
    print(lir.intercept_)

def pipeline_demo():
    x = np.random.uniform(-3, 3, size=100)
    X = x.reshape(-1, 1)
    y = 2.5 * x ** 2 + 3 * x + 2 + np.random.normal(0, 1, 100)
    poly_reg = Pipeline([("poly", PolynomialFeatures(degree=2)),
                         ("std_scaler", StandardScaler()),
                         ("lin_reg", LinearRegression())])
    poly_reg.fit(X,y)
    y_pridect = poly_reg.predict(X)
    print(y_pridect)


def learn_curve(lin_reg):
    x = np.random.uniform(-3, 3, size=100)
    X = x.reshape(-1, 1)
    y = 0.1 * x ** 2 + 3 * x + 2 + np.random.normal(0, 1, 100)
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=10)
    train_score = []
    test_score = []
    for i in range(1,X.size+1):
        lin_reg.fit(X_train[:i],y_train[:i])
        y_train_predict = lin_reg.predict(X_train[:i])
        train_score.append(mean_squared_error(y_train[:i],y_train_predict))

        y_test_predict = lin_reg.predict(X_test)
        test_score.append(mean_squared_error(y_test,y_test_predict))

    plt.plot([i for i in range(1,len(train_score)+1)],np.sqrt(train_score),label='train')
    plt.plot([i for i in range(1,len(test_score)+1)],np.sqrt(test_score),label='test')
    plt.legend()
    plt.axis([1,100,0,4])
    plt.show()

def cross_val_score_demo():
    data = datasets.load_digits()
    x,y = data.data,data.target
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    best_k, best_p, best_score = 0, 0, 0
    for k in range(2, 11):
        for p in range(1, 6):
            knn_clf = KNeighborsClassifier(weights="distance", n_neighbors=k, p=p)
            scores = cross_val_score(knn_clf, X_train, y_train)
            score = np.mean(scores)
            if score > best_score:
                best_k, best_p, best_score = k, p, score

    print("Best K =", best_k)
    print("Best P =", best_p)
    print("Best Score =", best_score)

x = np.random.normal(-3,3,100)
X = x.reshape(-1,1)
random.seed(666)
y = 0.5 * x + 1 +np.random.normal(0,1,100)

def ridge_regression_demo(degree,alpha):

    def ridgeRegression(degree,alpha):
        return Pipeline(
            [
                ('fea',PolynomialFeatures(degree=degree)),
                ('scaler',StandardScaler()),
                ('rid_rlg',Ridge(alpha=alpha))
             ]
        )
    X_train,X_test,y_train,y_test = train_test_split(X,y)

    rid_rlg1 = ridgeRegression(degree,alpha)
    return rid_rlg1.fit(X_train,y_train)

def plot_mode(alg,title):
    plot_x = np.linspace(-3,3,num=100).reshape(100,1)
    plot_y = alg.predict(plot_x)
    plt.scatter(X,y)
    plt.plot(plot_x[:],plot_y,color='r')
    plt.title(title)
    plt.axis([-3,3,-1,2.5])
    plt.show()

def plot_more(plots):
    fig, ax_big = plt.subplots( figsize=(30, 20))
    for i,draw in enumerate(plots):
        ax = fig.add_subplot(3, 4, i+1)
        ax.plot(draw)
    plt.show()

if __name__ == "__main__":
    alg1 = ridge_regression_demo(20,0.0001)
    alg2 = ridge_regression_demo(20,1)
    alg3= ridge_regression_demo(20,50)
    alg4= ridge_regression_demo(20,100)

    plot_mode(alg1,'alpha=0.0001')
    plot_mode(alg2,'alpha=1')
    plot_mode(alg3,'alpha=50')
    plot_mode(alg4,'alpha=100')