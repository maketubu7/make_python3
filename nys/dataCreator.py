# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:19
# @Author  : dengwenxing
# @Software: PyCharm

import sys, logging,hashlib,random
from faker import Faker
from nys.labelConsts import *
from nys import fieldCreator
import pandas as pd
from functools import reduce
from pandas.core.frame import DataFrame
import numpy as np

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

f = Faker(locale='zh_CN')
funs = fieldCreator.initFunc()

def createData(*cols,num=None):
    '''
    :param cols:
    :param num: 伪造边得数据的时候要传入节点的最少数量, 若不传入则为生成点的数据
    :通过num值判定是否为生成边或者是点
    :return:
    '''
    if not num:
        res = []
        for col in cols:
            res.append(funs[col]())
        return res
    else:
        res = {}
        for col in cols:
            keys = []
            for i in range(num):
                keys.append(funs[col]())
            res[col] = keys
        return res

def path(v):
    return u"E:\python_workspace\make_python3\data\%s.csv"%v

def jid(tablename,index):
    return str(random.randint(1, 9)) + str(vertex_index[tablename] + index)

def write_csv(df,tablename):
    df.to_csv(path(tablename), encoding='utf-8',index=None)

def read_csv(v):
    df = pd.read_csv(path(v))
    return df

def sample_shuffle(df,edgeType="common"):
    '''减少数据并重复数据量'''
    sampleRatio = 0.2 if edgeType != "common" else 0.5
    sampledf = df.sample(frac=sampleRatio)
    res = reduce(lambda x,y: pd.concat([x,y],axis=0),[sampledf for i in range(int(1/sampleRatio))])
    return res

def edge_from_tuili_node(start_df,end_df,edge_schema,tablename):
    ''' 通过推理前置表得到推理结果表 '''
    start_df = start_df[[0,2,3]]
    end_df = end_df[[0,2,3]]
    on_key = list(end_df)[2]
    groupfield = edge_zd + edge_schema[:2]
    res = pd.merge(start_df,end_df,left_on=on_key,right_on=on_key)
    res = res[res["sfzh_x"]!=res["sfzh_y"]]
    res["start_jid"] = np.where(res["sfzh_x"] > res["sfzh_y"], res["start_jid_y"],res["start_jid_x"])
    res["end_jid"] = np.where(res["sfzh_x"] > res["sfzh_y"], res["start_jid_x"],res["start_jid_y"])
    res["sfzh1"] = np.where(res["sfzh_x"] > res["sfzh_y"], res["sfzh_y"],res["sfzh_x"])
    res["sfzh2"] = np.where(res["sfzh_x"] > res["sfzh_y"], res["sfzh_x"],res["sfzh_y"])
    res.drop(labels=["sfzh_x","sfzh_y","start_jid_x","start_jid_y"], axis=1, inplace=True)
    res.drop_duplicates(inplace=True)
    res.drop(labels=[on_key],axis=1, inplace=True)
    # df = res.head(20).groupby(groupfield)
    dfs = []
    for key, sub_df in res.groupby(groupfield):
        tmp = list(key)
        tmp.append(len(sub_df))
        dfs.append(tmp)
    df = pd.DataFrame(dfs,columns=edge_zd+edge_schema)
    df.drop_duplicates(edge_drop[tablename],inplace=True)
    return df

def edge_from_common_node(start_df, end_df,edge_schema,tablename):
    edgeType = 'pre_tuili' if tablename in edge_type["pre_tuili"] else "common"
    start_key = edge_schema[0]
    end_key = edge_schema[1]
    other_keys = edge_schema[2:]
    pre_start = sample_shuffle(start_df[[0, 1]], edgeType=edgeType)
    pre_end = sample_shuffle(end_df[[0, 1]], edgeType=edgeType)
    start_node = None
    end_node = None
    if isinstance(pre_start,DataFrame):
        start_node = list(pre_start[edge_schema[0]])
        random.shuffle(start_node)
    if isinstance(pre_end,DataFrame):
        end_node = list(pre_end[edge_schema[1]])
        random.shuffle(end_node)
    # 得到随机匹配的一对多，多对一的关系
    pre_dic = zip(start_node, end_node)
    pre = pd.DataFrame(list(pre_dic), columns=edge_schema[:2])
    # join与开始结束节点的jid, 主键进行join,获取边的关系
    left = pd.merge(pre, pre_start, left_on=start_key, right_on=start_key)
    res = pd.merge(left, pre_end, left_on=end_key, right_on=end_key)
    res.rename(columns={"jid_x": "start_jid", "jid_y": "end_jid"}, inplace=True)
    other_values = createData(*other_keys, num=len(res))
    if other_keys:
        for key in other_keys:
            res[key] = other_values[key]
    res.drop_duplicates(edge_drop[tablename],inplace=True)
    return res



vertex_zd = ['jid']
def get_vertex_data(num=100000,tablename=None):
    if tablename:
        schema = vertex_table_info[tablename]
        infos = []
        for i in range(num):
            info = createData(*schema)
            infos.append(info)
        df = pd.DataFrame(infos,columns=schema)
        df["jid"] = [jid(tablename,i) for i in range(len(df))]
        df.drop_duplicates(vertex_drop[tablename],inplace=True)
        write_csv(df[vertex_zd+schema],tablename)
    else:
        print("no label name please input")
        sys.exit(1)

edge_zd = ["start_jid", "end_jid"]
def get_edge_data(tablename=None):
    if tablename:
        v1, v2 = edge_map_info[tablename]
        schema = edge_table_info[tablename]
        # E:\python_workspace\make_python3\data
        try:
            start_node = read_csv(v1)
            end_node = read_csv(v2)
            if tablename in edge_type["tuili"]:
                df = edge_from_tuili_node(start_node, end_node, schema, tablename)
            else:
                df = edge_from_common_node(start_node, end_node, schema, tablename)
            write_csv(df[edge_zd+schema],tablename)
        except Exception as e:
            logger.error("read csv file error %s, %s, you must create relate nodes at first!"%(v1, v2),e)
    else:
        logger.info("no label name please input")

if __name__ == '__main__':
    # get_edge_data("edge_person_reserve_airline")
    # get_vertex_data(tablename="vertex_trainline",num=100)
    # get_edge_data(tablename="edge_person_reserve_trainline")
    # start_df = read_csv("edge_person_reserve_airline")
    # end_df = read_csv("edge_person_reserve_airline")
    # res = edge_from_tuili_node(start_df,end_df,["sfzh1","sfzh2","num"],1)
    # print(res[0])
    # print(df)

    get_edge_data(tablename="edge_person_withtrain_person")