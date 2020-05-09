# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 17:05
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : readMysql.py
# @Software: PyCharm
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/spider_demo')


def read_mysql(tablename):
    sql = "select * from {}".format(tablename)
    df = pd.read_sql_query(sql,engine)
    print(df["topic_id"].head())
    return df

def save_mysql(df,tablename):
    try:
        df.to_sql(tablename,engine,if_exists='replace',index=False,chunksize=1024)
    except:
        pass

if __name__ == "__main__":
    # read_mysql('topic')
    ##save_mysql()
    pass