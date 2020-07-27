# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 17:39
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : deal_case_link_info.py
# @Software: PyCharm

import pandas as pd
import functools

def make_arr(ajbh,t):
    return [ajbh,t[0],t[1]]
root_path = 'C:\\Users\\lenovo\\Desktop\\case_data_all\\'
def do():
    df = pd.read_excel(root_path+'case_link_source1.xlsx',sheetname='Sheet1',dtype='str')
    res = []
    for ajbh, sub in df.groupby('ajbh'):
        nodes = list(sub['bank_code'].str.split(','))[0]
        types = list(sub['bank_type'].str.split(','))[0]
        if len(nodes) == len(types):
            tmp1 = list(zip(types,nodes))
            tmp2 = list(map(lambda t:make_arr(ajbh,t),tmp1))
            res.append(tmp2)
    dfs = functools.reduce(lambda a,b:a+b,res)
    dfs = list(filter(lambda a: a[1]=='qq' or a[1]=='wechat' or a[1] =='alipay',dfs))
    df = pd.DataFrame(dfs,columns=['ajbh','type','value'])
    df.drop_duplicates(inplace=True)
    df.to_csv(root_path+'case_link_source2.csv',header=True,index=False)

def do_phone():
    df = pd.read_excel(root_path+'case_link_source1.xlsx',sheetname='Sheet3',dtype='str')
    res = []
    for ajbh, sub in df.groupby('ajbh'):
        nodes = list(sub['phone'].str.split(','))[0]
        nodes = list(filter(lambda a: len(a)<=11, nodes))
        for node in nodes:
            res.append([ajbh,'phone',node])
    df = pd.DataFrame(res,columns=['ajbh','type','value'])
    df.drop_duplicates(inplace=True)
    df.to_csv(root_path+'case_link_source3.csv',header=True,index=False)

def do_person():
    df = pd.read_excel(root_path+'case_link_source_all.xlsx',sheetname='Sheet4',dtype='str')
    res = []
    for ajbh, sub in df.groupby('ajbh'):
        nodes = list(sub['sfzh'].str.split(','))[0]
        for node in nodes:
            res.append([ajbh,'person',node])
    df = pd.DataFrame(res,columns=['ajbh','type','value'])
    df.drop_duplicates(inplace=True)
    df.to_csv(root_path+'case_link_source4.csv',header=True,index=False)

def vase():
    df = pd.read_excel(root_path + 'case_link_source_all_new.xlsx', sheetname='Sheet6', dtype='str')
    df['ajmc'] = df['xm']+df['ajlb']+'受骗案'
    df.drop('xm',axis=1,inplace=True)
    df['jyaq_bk'] = df['jyaq'].str.replace('\n','').replace('\r','').replace('\r\n','').replace(',','，').replace('\t','')
    df.drop('jyaq',axis=1,inplace=True)
    df.to_csv(root_path + 'zp_case_new.csv', header=True, index=False,sep='|')

if __name__ == "__main__":
    df = vase()