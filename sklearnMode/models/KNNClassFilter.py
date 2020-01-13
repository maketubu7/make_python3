# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 20:53
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : KNNClassFilter.py
# @Software: PyCharm
import sys
import numpy as np
class knnClassFilter():

    def __init__(self,k):
        assert k >= 1, "k must be vaild"
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self,X_train,y_train):
        assert X_train.shape[0] == y_train.shape[0], "the size of X_train must be equal to the size of y_train"
        assert self.k <= X_train.shape[0], "the size of X_train must be at least k."
        self.X_train = X_train
        self.y_train = y_train
        return self

    def predict(self,X_predict):
        assert self._X_train is not None and self._y_train is not None, "must fit before predict!"
        assert X_predict.shape[1] == self._X_train.shape[1], "the feature number of X_predict must be equal to X_train"

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)
    def _predict(self,x):
        pass



if __name__ == "__main__":
    pass