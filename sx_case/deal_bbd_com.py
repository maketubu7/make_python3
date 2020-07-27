# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, json,urllib,time
import threading,functools
import pandas as pd



cookie = 'JSESSIONID=8E2C10DCCD3406D7E24C1F215F513F89'
root_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'openapi.bbdops.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }

save_path = 'C:\\Users\\lenovo\\Desktop\\com_data\\{}'

def add_save_path(name,suffix='.csv'):
    return save_path.format(name+suffix)

def get_keys(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        f = lambda qq: qq.replace('\r\n', '').replace('\r', '').replace('\n', '').strip()
        res = set([f(v) for v in lines])
    return res

def write_json2txt(res,name):
    with open(add_save_path(name),'w') as f:
        json.dump(res,f,ensure_ascii=False)

def read_json(path):
    with open(path,'r') as f:
        res = json.load(f)
    return res

def get_all_comname(file):
    file = add_save_path(file,suffix='.txt')
    res = []
    with open(file,'r',encoding='utf8') as f:
        lines = f.readlines()
        for com_name in lines:
            com_name = com_name.replace("\n","")
            res.append(com_name)
    return res


def deal_shareholder():
    res = []
    root_url = """ http://openapi.bbdops.com/openapi/test/runInterface.action?method=get&url=http://dataapi.bbdservice.com/api/bbd_qyxx_gdxx2/&headers=[]&params=[{"key":"company","value":"%s"},{"key":"qyxx_id","value":""},{"key":"appkey","value":"2c8e7mfscf57ajxh7fi49ilyanmmf0bs"},{"key":"page","value":""},{"key":"pageSize","value":""},{"key":"start","value":""},{"key":"end","value":""},{"key":"internal","value":""}] """
    i = 0
    all_coms = get_all_comname('dk_sub')
    for com_name in all_coms:
        url = root_url % (com_name)
        text = requests.get(url, headers=root_header).text
        source_data = json.loads(text)
        if source_data:
            if source_data['data']:
                tmp_res = json.loads(source_data['data'])
                coms = tmp_res['results']
                i += 1
                print(i,com_name)
                for item in coms:
                    item['company']=com_name
                    res.append(item)
    df = pd.DataFrame(res)
    df.to_csv(add_save_path('dk_sub_shareholder'),sep='\t',index=None)

def law_jud_doc():
    root_url = 'http://openapi.bbdops.com/openapi/test/runInterface.action?method=get&url=http://dataapi.bbdservice.com/api/bbd_legal_adjudicative_documents&headers=[]&params=[{"key":"company","value":"%s"},{"key":"qyxx_id","value":""},{"key":"page","value":""},{"key":"pageSize","value":""},{"key":"start","value":""},{"key":"end","value":""},{"key":"appkey","value":"2c8e7mfscf57ajxh7fi49ilyanmmf0bs"},{"key":"internal","value":""}]'
    all_coms = get_all_comname('all_his_shareholder_com')
    i = 0
    res = []
    for com_name in all_coms:
        url = root_url % (com_name)
        text = requests.get(url, headers=root_header).text
        source_data = json.loads(text)
        if source_data:
            if source_data['data']:
                tmp_res = json.loads(source_data['data'])
                coms = tmp_res['results']
                i += 1
                print(i,com_name)
                for item in coms:
                    item['notice_content'] = item['notice_content'].replace('\r\n','').replace('\n','')
                    res.append(item)
        # if i > 10 : break
    df = pd.DataFrame(res)
    df.to_csv(add_save_path('all_his_shareholder_law_jud_doc'),sep='\t',index=None)

def get_his_shareholder():
    root_url = 'http://openapi.bbdops.com/openapi/test/runInterface.action?method=get&url=http://dataapi.gateway.bbdservice.com/api/bbd_relations/getHisInvest/&headers=[]&params=[{"key":"bbd_qyxx_id","value":"%s"},{"key":"appkey","value":"2c8e7mfscf57ajxh7fi49ilyanmmf0bs"},{"key":"page","value":""},{"key":"pageSize","value":""},{"key":"start","value":""},{"key":"end","value":""},{"key":"internal","value":""}]'
    all_coms = get_all_comname('all_qyxx_id')
    i = 0
    res = []
    for com_name in all_coms:
        url = root_url % (com_name)
        i += 1
        print(url)
        try:
            text = requests.get(url, headers=root_header).text
            source_data = json.loads(text)
            data_res = json.loads(source_data['data'])
            print(i,data_res)
            if data_res:
                data_info = data_res['data']
                for item in data_info:
                    res.append(item)
        except:
            print(i,com_name)
            continue

    df = pd.DataFrame(res)
    df.to_csv(add_save_path('all_com_his_shareholder'),sep='\t',index=None)

def get_com_info():
    root_url = 'http://openapi.bbdops.com/openapi/test/runInterface.action?method=get&url=http://dataapi.bbdservice.com/api/bbd_qyxx/&headers=[]&params=[{"key":"company","value":"%s"},{"key":"qyxx_id","value":""},{"key":"appkey","value":"2c8e7mfscf57ajxh7fi49ilyanmmf0bs"},{"key":"credit_code","value":""},{"key":"regno","value":""},{"key":"internal","value":"true"}]'
    all_coms = get_all_comname('all_his_shareholder_com')
    i = 0
    res = []
    for com_name in all_coms:
        url = root_url % (com_name)
        print(url)
        try:
            text = requests.get(url, headers=root_header).text
            source_data = json.loads(json.loads(text)['data'])
            jbxx = source_data['results'][0]['jbxx']
            print(jbxx)
            if jbxx:
                res.append({'com':com_name,'bbd_qyxx_id':jbxx['bbd_qyxx_id']})
        except:
            print(com_name)
            continue
    df = pd.DataFrame(res)
    df.to_csv(add_save_path('all_his_sharer_com_bbd_qyxx_id'),sep='\t',index=None)


def his_sharer_out_invest():
    root_url = 'http://openapi.bbdops.com/openapi/test/runInterface.action?method=get&url=http://dataapi.gateway.bbdservice.com/hongjing7/api/hongjing/0/financial/historyshareholder_out_invest&headers=[]&params=[{"key":"qyId","value":"%s"},{"key":"appkey","value":"2c8e7mfscf57ajxh7fi49ilyanmmf0bs"}]'
    all_coms = get_all_comname('all_his_sharer_com_qyxx_id')
    i = 0
    res = []
    for com_name in all_coms:
        url = root_url % (com_name)
        i += 1
        print(url)
        try:
            text = requests.get(url, headers=root_header).text
            source_data = json.loads(text)
            data_res = json.loads(source_data['data'])
            data_info = data_res['data']
            print(data_info)
            if data_info:
                for item in data_info:
                    res.append(item)
        except:
            print(i, com_name)
            continue

    df = pd.DataFrame(res)
    df.to_csv(add_save_path('all_his_shareholder_out_invest'), sep='\t', index=None)

if __name__ == '__main__':
    deal_shareholder()