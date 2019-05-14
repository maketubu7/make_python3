from elasticsearch import Elasticsearch

ip = "192.168.89.77"
port = "9200"

mapping = {'properties':{
    'title':{
        'type':'text',
        'analyzer': 'ik_max_word',
        'search_analyzer': 'ik_max_word'
}}}

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
# es.indices.delete(index='news',ignore=[400,404])
# es.indices.create(index='news',ignore=[400,404])
# result = es.indices.put_mapping(index='news',doc_type='politics',body=mapping)
datas=[
    {
        'title':'美国留给伊拉克的是个烂摊子吗',
        'url':r'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date':'2011-12-16'
    },
    {
        'title':'公安部：各地校车将享最高路权',
        'url':r'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'date':'2011-12-16'
    },
    {
        'title':'中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url':r'https://news.qq.com/a/20111216/001044.htm',
        'date':'2011-12-17'
    },
    {
        'title':'中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url':r'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date':'2011-12-18'
    }
]

# for data in datas:
#     es.index(index='news',doc_type='politics',body=data)

result = es.search(index='news', doc_type='politics')
print(result)
print('------------------------------------------')

dsl = {'query':{'match':{'title':'中国 领事馆'}}}
result = es.search(index='news', doc_type='politics',body=dsl)
print(result)
print('------------------------------------------')

# 四种查询
# term 精确查询
term_query = {
    'query':{
        'term':{
            'title':u'美国留给伊拉克的是个烂摊子吗'
        }
    }
}

# 模糊查询 并按date字段进行倒序排序 match_phrase 短语搜索 短语必须保持一致性
match_query = {
    'query':{
        'match':{
            'title':'中国'
        }
    },
    'sort': [
     {
       'date': {
         'order': 'desc'
       }
     }
   ]
}


# match_all所有查询
match_all_query = {
    'query':{
        'match_all':{}
    }
}

# multi_match 多值模糊查询
multi_match_query = {
    'query':{
        'multi_match':{
            'query':'中国 公安',
            'fields':['title^2','url']
            }
    }
}

# {
#     "multi_match": {
#         "query":                "Quick brown fox",    查询的内容
#         "type":                 "best_fields",    三种模式 best_fields 、 most_fields 和 cross_fields （最佳字段、多数字段、跨字段）
#         "fields":               [ "title^2", "body" ],  查询字段 对title进行权重提升  默认权重为1
#         "tie_breaker":          0.3,
#         "minimum_should_match": "30%" 
#     }
# }


# 布尔过滤器 
# must 所有条件必须满足
# should 满足任意一个条件
# must_not 所有条件都不满足
bool_query = {
    "query" : {
        "bool": {    
            "must": [
                {"match" : { "title" : "中国" }},
                {"match" : { "title" : "韩" }}
            ]
        }
    }
}

bool_union_query = {
    "query" : {
        "bool": {    
            "must": [
                {"match" : { "title" : "中国" }}
            ],
            "must_not":[
                {"match":{"title":"韩"}}
            ]
        }
    }
}


res = es.search(index='news', doc_type='politics',body=term_query)
print(res)

print('------------match--------------')
res = es.search(index='news', doc_type='politics',body=match_query)
print(res)

print('-------------match_all-------------')
res = es.search(index='news', doc_type='politics',body=match_all_query)
print(res)

print('------------multi_match--------------')
res = es.search(index='news', doc_type='politics',body=multi_match_query)
print(res)

print('--------------bool_query------------')
res = es.search(index='news', doc_type='politics',body=bool_query)
print(res)
print('------------bool_union--------------\n')
res = es.search(index='news', doc_type='politics',body=bool_union_query)
print(res)








