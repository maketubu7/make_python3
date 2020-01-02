# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:19
# @Author  : dengwenxing
# @Software: PyCharm

import sys, logging,hashlib,random
from faker import Faker
from nys.labelConsts import *
from nys import fieldCreator
import pandas as pd

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

f = Faker(locale='zh_CN')
funs = fieldCreator.initFunc()

def createData(*cols,num=None):
    '''
    :param cols:
    :param num: 伪造边得数据的时候要传入节点的最少数量, 若不传入则为生成点的数据
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
    return "E:\python_workspace\make_python3\data\%s.csv"%v

def write_csv(df,tablename):
    df.to_csv(path(tablename), encoding='utf-8',index=None)

def read_csv(v):
    df = pd.read_csv(path(v))
    return df

def edge_from_node(start_df, end_df,edge_schema):
    start_key = edge_schema[0]
    end_key = edge_schema[1]
    other_keys = edge_schema[2:]
    start_node = list(start_df[edge_schema[0]])
    end_node = list(end_df[edge_schema[1]])
    random.shuffle(start_node)
    random.shuffle(end_node)
    cou = len(start_node) if len(start_node) < len(end_node) else len(end_node)
    pre_dic = zip(start_node, end_node[:cou])
    pre = pd.DataFrame(list(pre_dic),columns=edge_schema[:2])
    left = pd.merge(pre,start_df[[0,1]],left_on=start_key, right_on=start_key)
    res = pd.merge(left,end_df[[0,1]],left_on=end_key, right_on=end_key)
    res.rename(columns={"jid_x":"start_jid","jid_y":"end_jid"},inplace=True)
    other_values = createData(*other_keys,num=cou)
    for key in other_keys:
        res[key] = other_values[key]
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
        df["jid"] = [int(vertex_index[tablename]+i) for i in range(len(df))]
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
            start_node = read_csv(v1)[[0,1]]
            end_node = read_csv(v2)[[0,1]]
            df = edge_from_node(start_node, end_node, schema)
            write_csv(df[edge_zd+schema],tablename)
        except Exception as e:
            logger.error("read csv file error %s, %s, you must create relate nodes at first!"%(v1, v2),e)
    else:
        logger.info("no label name please input")



if __name__ == '__main__':
    # get_vertex_data(tablename="vertex_person")
    # get_vertex_data(tablename="vertex_phonenumber")
    get_edge_data(tablename="edge_phone_smz_person")
    # print(hashlib.sha256("511622199310226471".encode("utf-8")).hexdigest())

