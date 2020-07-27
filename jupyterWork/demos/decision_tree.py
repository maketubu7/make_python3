# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 19:04
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : decision_tree.py
# @Software: PyCharm

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier



if __name__ == "__main__":
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X = X[:,2:]
    dt_clf = DecisionTreeClassifier()
    dt_clf.fit(X,y)

