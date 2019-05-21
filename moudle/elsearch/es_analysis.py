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
# res = es.indices.put_mapping(index='megacorp',doc_type='employee',body=set_mapping)
# print(res)
res = es.search(index='megacorp',doc_type='employee',body=agg_query)
print(res)


# 对last_name=smith 进行聚合
agg_filter_query = {
        "query": {
            "match": {
            "last_name": "smith"
            }
        },
        "aggs": {
            "all_interests": {
            "terms": {
                "field": "interests"
            }
            }
        }
        }
print('-------------agg_filter_query-------------')
res = es.search(index='megacorp',doc_type='employee',body=agg_filter_query)
print(res)

# 二次聚合 先对兴趣做聚合，在对每个兴趣的年龄做聚合
agg_twice_query = {
    "aggs" : {
        "all_interests" : {
            "terms" : { "field" : "interests" },
            "aggs" : {
                "avg_age" : {
                    "avg" : { "field" : "age" }
                }
            }
        }
    }
}
print('-------------agg_twice_query-------------')
res = es.search(index='megacorp',doc_type='employee',body=agg_twice_query)
print(res)
# 结果集
data = res['aggregations']['all_interests']['buckets']
print('-------------agg_twice_query_result-------------')
print(sorted(data,key=lambda x: x['doc_count'], reverse=True))


# es.mget 根据id一次性返回过个结果 _source 参数可以设置返回所需的字段
mget_query = {
    'docs':[{
        '_index':'megacorp',
        '_doc_type':'employee',
        '_id':'AWozNixGrCQN1BwaEs8x'
    },{
         "_index" : "megacorp",
         "_type" :  "employee",
         "_id" :'AWozNi0prCQN1BwaEs80',
         "_source": "age"
      }]
}
mget_query2 = {'ids':['AWozNixGrCQN1BwaEs8x','AWozNi0prCQN1BwaEs80']}

res = es.mget(body=mget_query)
print(res)



