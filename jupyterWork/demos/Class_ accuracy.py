import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.multiclass import OneVsRestClassifier,OneVsOneClassifier
from sklearn.linear_model import LogisticRegression


class LogisticRegession:

    def __init__(self):
        """初始化Linear Regression模型"""
        self.coef_ = None
        self.intercept_ = None
        self._theta = None

    def _sigmoid(self,t):
        return 1 / (1 + np.exp(-t))

    def fit_bgd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """根据训练数据集X_train, y_train, 使用梯度下降法训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        def J(theta, X_b, y):
            y_hat = self._sigmoid(X_b.dot(theta))
            try:
                return np.sum(y*np.log(y_hat)+(1-y)*np.log(1-y_hat)) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            return X_b.T.dot(self._sigmoid(X_b.dot(theta))-y) / len(y)

        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):

            theta = initial_theta
            cur_iter = 0

            while cur_iter < n_iters:
                gradient = dJ(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient
                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break

                cur_iter += 1

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b, y_train, initial_theta, eta, n_iters)

        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        proba = self.predict_proba(X_predict)
        return np.array(proba>=0.5,dtype='int')

    def predict_proba(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return self._sigmoid(X_b.dot(self._theta))

    def score(self, X_test, y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""

        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)

    def __repr__(self):
        return "LogsiticRegression()"

def plot_all(X,y,log_reg):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color='r')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color='b')

    plt_x = np.linspace(4, 7, 100)
    plt_y = -(log_reg.intercept_ + log_reg.coef_[0] * plt_x) / log_reg.coef_[1]
    plt.plot(plt_x, plt_y)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(u'所有数据决策边界')
    plt.show()

def plot_test(X,y,log_reg):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color='r')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color='b')

    plt_x = np.linspace(4, 7, 100)
    plt_y = -(log_reg.intercept_ + log_reg.coef_[0] * plt_x) / log_reg.coef_[1]
    plt.plot(plt_x, plt_y)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(u'测试数据决策边界')
    plt.show()


def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1), )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)

## OvR OvO
def ovr_ovo_demo(multi_class='ovr',solver='lbfgs'):
    from sklearn.linear_model import LogisticRegression

    def PolynomialLogisticRegression(degree, multi_class=multi_class,solver=solver):
        return Pipeline([
            ('poly', PolynomialFeatures(degree=degree)),
            ('std_scaler', StandardScaler()),
            ('log_reg', LogisticRegression(multi_class=multi_class,solver=solver))])
    log_reg = PolynomialLogisticRegression(1,multi_class=multi_class,solver=solver)
    log_reg.fit(X_train,y_train)
    print(multi_class,log_reg.score(X_test,y_test))

def ovr_ovo_demo2(type = 'ovr'):
    def PolynomialLogisticRegression(degree):
        return Pipeline([
            ('poly', PolynomialFeatures(degree=degree)),
            ('std_scaler', StandardScaler()),
            ('log_reg', LogisticRegression())])
    log_reg = PolynomialLogisticRegression(1)
    reg = OneVsRestClassifier(log_reg)
    if type != 'ovr':
        reg = OneVsOneClassifier(log_reg)

    reg.fit(X_train,y_train)
    print(type,reg.score(X_test,y_test))

if __name__ == '__main__':
    iris = datasets.load_digits()
    X = iris.data
    y = iris.target

    X = X[:,:]
    y = y
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    log_reg = LogisticRegession()
    log_reg.fit_bgd(X_train,y_train)
    print('二分类',log_reg.score(X_test,y_test))

    # plot_all(X,y,log_reg)
    # plot_test(X_test,y_test,log_reg)

    ##ovr ovo
    # ovr_ovo_demo()
    # ovr_ovo_demo(multi_class='multinomial',solver='newton-cg')

    ##ovr ovo
    ovr_ovo_demo2()
    ovr_ovo_demo2(type='ovo')




