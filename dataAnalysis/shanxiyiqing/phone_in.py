import pandas as pd
import os
import numpy as np



def get_all_files(domain):
    all_files = []
    for root, dirs, files in os.walk(domain):
        for file in files:
            all_files.append(os.path.join(root,file))
    return all_files

def text2df(filename,usecols=None,columns=None,drop_key=None):
    '''
    :param filename:
    :return:
    '''
    if not usecols:
        usecols = [1]
    if not columns:
        columns = ["phone"]
    assert len(usecols)==len(columns), 'usecols length must equal columns length'
    plist = []
    print(filename)
    with open(filename,'r',encoding='utf8') as f:
        try:
            lines = f.readlines()
            for line in lines[1:]:
                phone = [line.split(",")[i] for i in usecols]
                plist.append(phone)
        except:
            pass
        phones = pd.DataFrame(plist,columns=columns,index=None,dtype=np.str)
        if drop_key:
            phones.drop_duplicates(subset=drop_key,inplace=True)
        return phones


def deal_all_data(files):
    res = []
    for file in files:
        res.append(text2df(file,drop_key=["phone"]))
    df = pd.concat(res,axis=0)
    if isinstance(df, pd.DataFrame):
        df.drop_duplicates(["phone"],inplace=True)
        df["phone"] = df["phone"].astype(str)
        df.to_csv('phone_in_result.csv',index=None)


def deal_befor_file(files):
    '''得到之前在晋的名单'''
    dfs = []
    i = 8
    for file in files:
        i += 1
        df = text2df(file)
        save_csv(df,str(i),home='D:\\BBD\\tmp_data')
        dfs.append(df)
        # union_df = pd.concat(dfs,axis=0)
        # union_df.drop_duplicates(["phone"],inplace=True)
        # save_csv(union_df,'before')
        # plist = union_df["phone"].tolist()
        # return plist

def save_csv(df, filename, home='D:\\BBD\\result_data'):
    assert os.path.isdir(home), 'home must be dirs'
    res_home = '{}\\{}.csv'
    df.to_csv(res_home.format(home, str(filename)), index=None)


def read_csv(filename):
    df = pd.read_csv(filename, dtype=object, header=0)
    return df

def df_subtract_list(df,plist,key='phone'):
    tag = df[key].isin(plist)
    not_tag = [not r for r in tag]
    df = df[not_tag]
    save_csv(df,'result_filter')

def df_subtract_df(df1,df2,subset=None):
    '''
    :param df1: first dataframe
    :param df2: subtract dataframe
    :param subset: type list duplicates columns
    :return: pandas dataframe
    '''
    assert isinstance(subset,list), 'subset must be list'
    assert len(df1.dtypes)==len(df2.dtypes), 'columns must be equal'
    assert subset, 'subset must be define ["col1","col2",...]'

    df1 = df1.append(df2)
    df1 = df1.append(df2)
    res = df1.drop_duplicates(subset=subset,keep=False)
    return res

def union_csvs(files):
    dfs = []
    for file in files:
        df = read_csv(file)
        dfs.append(df)
    res = pd.concat(dfs,axis=0)
    if isinstance(res,pd.DataFrame):
        res.drop_duplicates(subset=["phone"], inplace=True)
    return res



if __name__ == '__main__':
    files = get_all_files('D:\\BBD\\tmp_data\\')
    # plist = deal_befor_file(files)
    df = read_csv('D:\\BBD\\result_data\\phone_in_result.csv')
    df2 = union_csvs(files)
    res = df_subtract_df(df,df2,subset=["phone"])
    save_csv(res,'result_filter')
    df_subtract_list(df,plist)