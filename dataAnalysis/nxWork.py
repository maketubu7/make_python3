# -*- coding:utf-8 -*-
# @Time    : 2019/12/27 11:25
# @Author  : dengwenxing
# @Software: PyCharm

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from dataAnalysis.pandasWork import fromFakerCall



#从dataFramae中加载数据到图
def dealCallGraph():
    callSchema = ["start_phone","end_phone","num"]
    call = pd.read_csv("E:\python_workspace\make_python3\data\call_detail.csv")
    call.columns = callSchema
    call[["start_phone", "end_phone"]] = call[["start_phone", "end_phone"]].astype(str)
    call[["num"]] = call[["num"]].astype(int)

    G = nx.from_pandas_dataframe(call,"start_phone","end_phone",["num"])
    # print(G.edge)
    # 网络结构中两点的最短路径
    # print(nx.shortest_path(G,'18007107813','18912141309'))

    #网络结构的度 拿到最大的度的节点
    degree = G.degree()
    degree = sorted(degree.items(),key=lambda tp: tp[1],reverse=True)
    print(degree[0])

    #最大子图
    connecteds = nx.connected_components(G)
    max_connect = max(connecteds,key=len)
    print(max_connect)
    nx.draw_networkx(G)
    plt.show()


if __name__ == '__main__':
    dealCallGraph()


