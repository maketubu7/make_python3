# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 13:50
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : confusion_matrix.py
# @Software: PyCharm

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def confusion_matrix(y_test,y_pridect):
    return np.array(
        [[TN(y_test,y_pridect),FP(y_test,y_pridect)],
         [FN(y_test,y_pridect),TP(y_test,y_pridect)]])

def TN(y_test,y_pridect):
    assert len(y_test) == len(y_pridect)
    return np.sum((y_test==0) & (y_pridect == 0))

def FN(y_test,y_pridect):
    assert len(y_test) == len(y_pridect)
    return np.sum((y_test==1) & (y_pridect == 0))

def TP(y_test,y_pridect):
    assert len(y_test) == len(y_pridect)
    return np.sum((y_test==1) & (y_pridect == 1))

def FP(y_test,y_pridect):
    assert len(y_test) == len(y_pridect)
    return np.sum((y_test==0) & (y_pridect == 1))

def precision_score(y_test,y_pridect):
    fP = FP(y_test,y_pridect)
    tp = TP(y_test,y_pridect)
    try:
        return tp/(tp+fP)
    except:
        return 0.0

def recall_score(y_test,y_pridect):
    fn = FN(y_test,y_pridect)
    tp = TP(y_test,y_pridect)
    try:
        return tp/(tp+fn)
    except:
        return 0.0

def f1_score(y_test,y_pridect):
    p_score = precision_score(y_test,y_pridect)
    re_score = recall_score(y_test,y_pridect)
    try:
        return 2*p_score*re_score/(p_score+re_score)
    except:
        return 0.0


def FPR(y_test,y_pridect):
    fP = FP(y_test,y_pridect)
    tn = TN(y_test,y_pridect)
    try:
        return fP/(tn+fP)
    except:
        return 0.0

def TPR(y_test,y_pridect):
    fn = FN(y_test,y_pridect)
    tp = TP(y_test,y_pridect)
    try:
        return tp/(tp+fn)
    except:
        return 0.0


def matrix_demo():
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target.copy()
    y[digits.target==9] = 1
    y[digits.target!=9] = 0

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
    log_reg = LogisticRegression()
    log_reg.fit(X_train,y_train)
    log_reg.score(X_test,y_test)

    y_pridect = log_reg.predict(X_test)
    return y_test,y_pridect

if __name__ == "__main__":
    y_test = np.array([1,1,1,0,0,0,1])
    y_pridect = np.array([1,1,1,1,0,0,1])

    mat = confusion_matrix(y_test,y_pridect)