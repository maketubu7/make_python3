from elasticsearch import Elasticsearch
import json
ip = "192.168.89.77"
port = "9200"

# es = Elasticsearch(['%s:%s'%(ip,port)])

data = ''' {
    "first_name" : "John",
    "last_name" :  "Smith",
    "age" :        25,
    "about" :      "I love to go rock climbing",
    "interests": [ "sports", "music" ]
} '''

data2 = ''' {
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
} '''

data3 = ''' {
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
} ''' 

data4 = ''' {
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
} ''' 

# /megacorp/employee/3

# es.create(index='megacorp',doc_type='employee',id=4,body=data4)
query = {'query': {'match_all': {}}}# 查找所有文档
query1 = {'query': {'match': {'first_name': 'Jane'}}}# 删除性别为女性的所有文档 
query2 = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档
query3 = {'query': {'match': {'first_name': 'Douglas'}}}# 查找名字叫做jack的所有文档

query4 = {"query" : {"bool": {"must": {"match" : {"last_name":"smith" }}, "filter": {"range" : {"age" : { "gt" : 30 }}}}}}
query5 = {"query" : {"match" : {"about" : "rock climbing"}}}
# result = es.search(index='megacorp',doc_type='employee',body=query1)
# print(result)

class EsManager():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def getInestance(self):
        ip = self.ip
        port = self.port
        return Elasticsearch(['%s:%s'%(ip,port)])

    def qurry(self,es,index,doc_type,query):
        res = es.search(index=index, doc_type=doc_type,body=query4)
        return res


EsManager = EsManager(ip,port)
es = EsManager.getInestance()

res = EsManager.qurry(es,'megacorp','employee',query)
print(res)


        

