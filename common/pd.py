import pandas as pd





def txt2csv(filename,special_data):
    list = []
    with open(r'F:\make_python3\channel\{}.txt'.format(filename)) as f:
        try:
            lines = f.readlines()
            for line in lines:
                phone = line.split(",")[0]
                list.append(phone)
        except:
            pass
        phones = pd.DataFrame(list,columns=['phone'],index=None)
        phones.drop_duplicates(["phone"],inplace=True)
        tag = phones["phone"].isin(special_data)
        not_tag = [not t for t in tag]
        return phones[not_tag]

def special_data(filename):
    list = []
    with open(r'F:\make_python3\channel\{}.txt'.format(filename)) as f:
        try:
            lines = f.readlines()
            for line in lines:
                phone = line.split(",")[0]
                list.append(phone)
        except:
            pass
        return list


if __name__ == '__main__':
    filenames = ['29','100']
    files = []
    special_data = special_data("109")

    for file in filenames:
        tmp = txt2csv(filename=file,special_data=special_data)
        files.append(tmp)
    res = pd.concat(files,axis=0)

    dfs = []
    for key, sub_df in res.groupby(["phone"]):
        tmp = []
        tmp.append(key)
        tmp.append(len(sub_df))
        dfs.append(tmp)
    # print(dfs)
    res = pd.DataFrame(dfs,columns=["phone","num"])
    res = res[res['num']>=4]
    res.to_csv('res.csv',index=None)



