# es 的一些分析功能
from elasticsearch import Elasticsearch
import json
from collections import OrderedDict
ip = "192.168.89.77"
port = "9200"

class EsManager():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def getInestance(self):
        ip = self.ip
        port = self.port
        return Elasticsearch(['%s:%s'%(ip,port)])

    def qurry(self,es,index,doc_type,query):
        res = es.search(index=index, doc_type=doc_type,body=query)
        return res

es = EsManager(ip, port).getInestance()

datas = [
    {
        "first_name" : "John",
        "last_name" :  "Smith",
        "age" :        25,
        "about" :      "I love to go rock climbing",
        "interests": [ "sports", "music" ]
    },
    {
        "first_name" :  "Jane",
        "last_name" :   "Smith",
        "age" :         32,
        "about" :       "I like to collect rock albums",
        "interests":  [ "music" ]
    },
    {
        "first_name" :  "Douglas",
        "last_name" :   "Fir",
        "age" :         35,
        "about":        "I like to build cabinets",
        "interests":  [ "forestry","football"]
    },
    {
        "first_name" :  "deng",
        "last_name" :   "Fir",
        "age" :         35,
        "about":        "I like to build cabinets",
        "interests":  [ "forestry","basketball"]
    },
]
# es.indices.create(index='megacorp')
# for data in datas:
#     es.index(index='megacorp',doc_type='employee',body=data)

''' Fielddata is disabled on text fields by default. Set fielddata=true '''
'''  这个报错是ES5.X以后 默认对text 类型的无法进行聚合 需要进行设置如下 '''
''' curl -XPUT 'http://192.168.89.77:9200/megacorp/_mapping/employee' -d '{"properties":{"interests":{"type":"text","fielddata":true}}}' '''
agg_query = {"size":0, "aggs":{"all_interests":{"terms":{ "field": "interests" }}}}

# 修改对应的默认的设置 es.indices.put_mapping(index=, doc_type=, body=)
set_mapping = {"properties":{"interests":{"type":"text","fielddata":True}}}
print('--------------aggs-------------------')
res = es.indices.put_mapping(index='megacorp',doc_type='employee',body=set_mapping)
print(res)
res = es.search(index='megacorp',doc_type='employee',body=agg_query)
print(res)
