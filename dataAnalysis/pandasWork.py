# -*- coding:utf-8 -*-
# @Time    : 2019/12/26 17:20
# @Author  : dengwenxing
# @Software: PyCharm

import pandas as pd
import dataAnalysis.tools as tool
import networkx as nx
import numpy as np

#读取csv
def test():
    df1 = pd.read_csv("E:\python_workspace\make_python3\data\call.csv",header=None,sep=",")
    df2 = pd.read_csv("E:\python_workspace\make_python3\data\call2.csv",header=None,sep=",")

    #修改列名 列的数据类型
    df1.columns=["start_phone","end_phone","num"]
    df2.columns=["start_phone","end_phone","num"]

    df1[["start_phone","end_phone"]] = df1[["start_phone","end_phone"]].astype(str)
    df1[["num"]] = df1[["num"]].astype(int)
    df2[["start_phone","end_phone"]] = df2[["start_phone","end_phone"]].astype(str)
    df2[["num"]] = df2[["num"]].astype(int)

    print(df1.dtypes)

    print("=======================筛选df[df['col'>value]]===========================")
    # df2 = df2[df2["num"]<70]
    # df1 = df1[df1["num"]>70]

    print(df1.head())

    print("====================插入一列 赋予新的值================")
    df1.insert(3,"city","成都")
    df2.insert(3,"city","德阳")
    df1[["city"]] = df1[["city"]].astype(str)
    df2[["city"]] = df2[["city"]].astype(str)
    print(df1.head())


    print("====================插入一行 赋予新的值================")
    new = pd.DataFrame([["13658163843","110",1,"德阳"]],columns=["start_phone","end_phone","num","city"])
    df1 = df1.append(new, ignore_index=True)
    print(df1["end_phone"])

    print("====================dataFrame union====================")
    df = df1.append(df2)
    print(df)


    print("====================dataFrame join====================")
    join_df1 = pd.merge(df1,df2,on=["end_phone","start_phone"],how="inner",indicator=True)
    print(join_df1.head())

    print('==合并字段不一样时，选择参数left_on="key", right_on="key"==')
    join_df2 = pd.merge(df1,df2,left_on="start_phone",right_on="end_phone")
    print(join_df2)

    print('=======得到列名 list(df),[column for column in df]======')
    print(list(join_df1))
    print([column for column in join_df1])

    print('=======================选择某个值========================')
    df_select = join_df1[join_df1.end_phone=="10086"]
    print(df_select)

    print('=======================concat========================')
    df_concat = pd.concat([df1,df_select])
    # print(df_concat)

    print('=======================数值类型的详细描述信息========================')
    print(df1[["num"]].describe())


def fromFakerPerson(num=1000):
    personSchema = ["name","age","address"]
    sourcePerson = tool.getFakerPerson(num)
    df = pd.DataFrame(sourcePerson)
    return df[personSchema]

def fromFakerCall(num=1000):
    callSchema = ["start_phone","end_phone","num"]
    sourceCall = tool.getFakerCall(20)
    df = pd.DataFrame(sourceCall)
    df[callSchema].to_csv("E:\python_workspace\make_python3\data\call_detail.csv",index=None)
    return df[callSchema]

if __name__ == '__main__':
    print(fromFakerCall().head())








