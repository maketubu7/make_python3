# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 14:38
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : SIMPLE_PCA.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plot

from sklearn.decomposition import PCA as SK_PCA

class PCA():

    def __init__(self,n_component):
        assert n_component >= 1, 'n_component must be valid'
        self.n_component = n_component
        self.components_ = None

    ## 目标函数
    def __repr__(self):
        return 'PCA(n_component={})'.format(self.n_component)

    def fit(self,X,eta=0.01, n_iters = 1e4):
        assert self.n_component <= X.shape[1], \
            'n_component must not be greater than frature numbers of X'
        def f(w,X):
            return np.sum(X.dot(w)**2) / len(X)

        ## 将样例的均值归为0 便于后面计算
        def demean(X):
            return X - np.mean(X, axis=0)

        ## 梯度函数
        def df_math(w,X):
            return X.T.dot(X.dot(w)) * 2. / len(X)
        ## 单位方向函数
        def direction(w):
            return w / np.linalg.norm(w)

        def first_component(X, initial_w, epsilon=1e-8):
            w = direction(initial_w)
            iters = 0

            while iters < n_iters:
                gradient = df_math(w,X)
                last_w = w
                w = w + eta * gradient
                w = direction(w)

                if (abs(f(w,X) - f(last_w,X)) < epsilon):
                    break
            return w

        X_pca = demean(X)
        ## n行 X.shape[1] 列
        self.components_ = np.empty(shape=(self.n_component,X.shape[1]))
        for i in range(self.n_component):
            initial_w = np.random.random(X_pca.shape[1])
            w = first_component(X_pca, initial_w, eta)
            self.components_[i,:] = w
            X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w
        return self

    def transform(self,X):
        '''将给定的X，映射到各个主成分分量中，也就是降维去噪的操作'''
        ''' n->k维 的降维，取决于主成分的个数为几个，就降到多少维 '''
        assert X.shape[1] == self.components_.shape[1]
        return X.dot(self.components_.T)

    def inverse_transform(self,X):
        '''将转化后低维的X，反向映射到原来的特征空间中'''
        assert X.shape[1] == self.components_.shape[0]
        return X.dot(self.components_)

if __name__ == "__main__":
    X = np.empty((100, 3))
    X[:, 0] = np.random.uniform(0., 100., size=100)
    X[:, 1] = 0.75 * X[:, 0] + 3. + np.random.normal(0, 10., size=100)
    X[:, 2] = 0.75 * X[:, 0] + 3. + np.random.normal(0, 10., size=100)
    pca = PCA(2)
    pca.fit(X)
    x_project = pca.transform(X)

    sk_pca = SK_PCA(3)
    sk_pca.fit(X)
    sk_x_project = sk_pca.transform(X)
    sk_x_restore = sk_pca.inverse_transform(sk_x_project)