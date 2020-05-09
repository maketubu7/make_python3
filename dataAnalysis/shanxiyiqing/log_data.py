import pandas as pd
import os,time
import numpy as np


def exectime(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('exec_time: {}'.format(str(end_time-start_time)))
        return res
    return wapper

def get_all_files(domain):
    all_files = []
    for root, dirs, files in os.walk(domain):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

@exectime
def text2df(filename, usecols=None, columns=None, drop_key=None):
    '''
    :param filename:
    :return:
    '''
    if not usecols:
        usecols = [1]
    if not columns:
        columns = ["phone"]
    assert len(usecols) == len(columns), 'usecols length must equal columns length'
    plist = []
    print(filename)
    with open(filename, 'r', encoding='utf8') as f:
        try:
            lines = f.readlines()
            for line in lines[1:]:
                if line.startswith("#"):
                    continue
                phone = [line.split(" ")[i] for i in usecols]
                plist.append(phone)
        except:
            pass
        phones = pd.DataFrame(plist, columns=columns, index=None, dtype=np.str)
        if drop_key:
            phones.drop_duplicates(subset=drop_key, inplace=True)
        return phones


def save_csv(df,filename,home='D:\\BBD\\result_data'):
    assert os.path.isdir(home), 'home must be dirs'
    res_home = '{}\\{}.csv'
    df.to_csv(res_home.format(home,str(filename)),index=None)

def read_csv(filename):
    df = pd.read_csv(filename, dtype=object, header=0, encoding='utf8')
    return df


def findweb(data):
    if data:
        tmp = data.lower()
        return tmp.str.startswith("/web/")
    return False

def day_log_count():
    files = get_all_files("D:\\BBD\\log_filter_csv")
    print(files[0].split('\\')[-1][4:10])
    res = []
    for file in files:
        tmp = []
        df = read_csv(file)
        datestr = file.split('\\')[-1][4:10]
        count = len(df)
        tmp.append(datestr)
        tmp.append(count)
        res.append(tmp)
    df = pd.DataFrame(res,columns=['date','count'],dtype=object)
    save_csv(df,'day_of_count.csv')

def ip_count():
    files = get_all_files("D:\\BBD\\log_filter_csv")
    dfs = []
    for file in files:
        df = read_csv(file)
        df = df[df['status']=='200']
        dfs.append(df)
    res = pd.concat(dfs,axis=0)
    if isinstance(res,pd.DataFrame):
        save_csv(res,'all_detail')

if __name__ == '__main__':

    # files = get_all_files("D:\\BBD\\log_source_csv")
    # print(files[0])
    # for file in files:
    # print(file)
    # filename = file.split('\\')[-1].replace('.csv', '')
    # df = read_csv(file)
    # df = df[df['uri'].str.lower().str.startswith('/web/')]
    # if not df.empty:
    # save_csv(df, filename=filename, home="D:\\BBD\\log_filter_csv")
    ip_count()



