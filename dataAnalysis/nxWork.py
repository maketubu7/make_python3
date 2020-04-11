# -*- coding:utf-8 -*-
# @Time    : 2019/12/27 11:25
# @Author  : dengwenxing
# @Software: PyCharm
import functools

import pandas as pd
import networkx as nx
from networkx import DiGraph
import matplotlib.pyplot as plt
# from dataAnalysis.pandasWork import fromFakerCall



#从dataFramae中加载数据到图

def get_graph():
    callSchema = ["start_phone", "end_phone"]
    call = pd.DataFrame([[1,2],[1,3],[1,4],[2,1],[2,3],[3,4],[3,1],[1,5]])
    call.columns = callSchema
    call[["start_phone", "end_phone"]] = call[["start_phone", "end_phone"]].astype(str)

    G = nx.from_pandas_dataframe(call, "start_phone", "end_phone",create_using=DiGraph())
    nx.write_graphml(G,'call.graphml')
    return G

def dealCallGraphUnDirected():
    callSchema = ["start_phone","end_phone","num"]
    call = pd.read_csv("E:\python_workspace\make_python3\data\call_detail.csv")
    call.columns = callSchema
    call[["start_phone", "end_phone"]] = call[["start_phone", "end_phone"]].astype(str)
    call[["num"]] = call[["num"]].astype(int)

    G = nx.from_pandas_dataframe(call,"start_phone","end_phone",["num"])
    # print(G.edge)
    # 网络结构中两点的最短路径
    # print(nx.shortest_path(G,'15860771674','18816004256'))
    print("最短路径: ",nx.dijkstra_path(G,source="15860771674",target="18570546027"))
    print("最短距离: ",nx.dijkstra_path_length(G,source="15860771674",target="18570546027"))

    # 所有节点的最短路径
    all_short = nx.all_pairs_shortest_path(G)
    for v, path in all_short.items():
        pass
        # print(v, path)

    #网络结构的度 拿到最大的度的节点
    degree = G.degree()
    degree = sorted(degree.items(),key=lambda tp: tp[1],reverse=True)
    print(degree[0])

    #最大连通图
    connecteds = nx.connected_components(G)
    max_connect = max(connecteds,key=len)
    print("最大连通图：",max_connect)

    #最大连通子图最大连通子图
    max_connectsub = nx.connected_component_subgraphs(G)
    print(type(max_connectsub), len(list(max_connectsub)))
    print(list(max_connectsub))


def dealCallGraphDirected():
    callSchema = ["start_phone", "end_phone", "num"]
    call = pd.read_csv("E:\python_workspace\make_python3\data\call_detail.csv")
    call.columns = callSchema
    call[["start_phone", "end_phone"]] = call[["start_phone", "end_phone"]].astype(str)
    call[["num"]] = call[["num"]].astype(int)

    G = nx.from_pandas_dataframe(call, "start_phone", "end_phone", ["num"], create_using=nx.DiGraph())

    # 弱连通图
    # weak_connect = nx.weakly_connected_components(G)
    # for conn in sorted(weak_connect,key=len, reverse=True):
    #     if len(conn) > 10:
    #         print("弱联通图：",conn)

    # 强连通图
    strong_connect = nx.strongly_connected_components(G)
    for conn in sorted(strong_connect,key=len, reverse=True):
        if len(conn) > 4:
            print("强联通图：", conn)

    # 子图
    nodes = ['18570546027','13702601124']
    subgraph = G.subgraph(nodes)
    print("包含某些点的子图：",subgraph.edge, subgraph.node)
    # print("所有子图：", G.subgraph())

    # 寻找初度为0的边
    out_zero = [k for k, v in G.out_degree().items() if v == 0]
    print('出度为0的边：', out_zero)

    out_two = [k for k, v in G.out_degree().items() if v > 1]
    print('出度大于2的边：', out_two)

    in_two = [k for k, v in G.in_degree().items() if v > 1]
    print('入度大于2的边：', in_two)

    degree_three = [k for k, v in G.degree().items() if v > 2]
    print('度大于3的边：', degree_three)

    print("图的密度：",nx.degree(G))

    degree_centra = nx.degree_centrality(G)
    max_degree_centra = sorted(degree_centra.items(),key=lambda tp: float(tp[1]), reverse=True)[0]
    print("节点度中心系数最大的点：", max_degree_centra)

    # 节点距离中心系数。通过距离来表示节点在图中的重要性，一般是指节点到其他节点的平均路径的倒数，
    # 这里还乘以了n-1。该值越大表示节点到其他节点的距离越近，即中心性越高
    closeness_centra = nx.closeness_centrality(G)
    max_closeness_centra = sorted(closeness_centra.items(), key=lambda tp: float(tp[1]), reverse=True)[0]
    print("节点距离中心系数最大的点：", max_closeness_centra)

    # 节点介数中心系数。在无向图中，该值表示为节点作占最短路径的个数除以((n-1)(n-2)/2)；
    # 在有向图中，该值表达为节点作占最短路径个数除以((n-1)(n-2))
    betweenness_centra = nx.betweenness_centrality(G)
    # print("节点介数中心系数",betweenness_centra)
    max_betweenness_centra = sorted(betweenness_centra.items(), key=lambda tp: float(tp[1]), reverse=True)[0]
    print("节点介数中心系数最大的点：", max_betweenness_centra)


def pagerank_demo():
    G = nx.read_graphml('call.graphml')
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    plt.show()
    # plt.savefig("g.pdf")
    res = nx.pagerank(G)
    return res

if __name__ == '__main__':

    res = pagerank_demo()
    print(functools.reduce(lambda x,y:x+y,res.values()))
    res = sorted(res.items(),key = lambda v:v[1],reverse=True)
    print(res)



