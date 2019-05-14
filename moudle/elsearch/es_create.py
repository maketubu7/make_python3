from elasticsearch import Elasticsearch
import json
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
# 创建index
# res = es.indices.create(index='news')
# print(res)

# 删除index
# res = es.indices.delete(index='news', ignore=[400,404])
# print(res)

# 插入文档 es.create() 方法需要指定id
data = {'title':u'美国留给伊拉克的是个烂摊子吗','url':r'http://view.news.qq.com/zt2011/usa_iraq/index.html'}
# data = {'title':'湖北考研分数被修改','url':r'https://baijiahao.baidu.com/s?id=1633394424199718152&wfr=spider&for=pc'}
# data = {'title':'湖北考研分数被修改','url':r'https://baijiahao.baidu.com/s?id=1633394424199718152&wfr=spider&for=pc'}
es.delete(index='news', doc_type='politics', id=1)
result = es.create(index='news', doc_type='politics', body=data, id=1)
# print(result)

# 更新数据 es.update() 指定id
# data = {
#     'title': '美国留给伊拉克的是个烂摊子吗',
#     'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
#     'date': '2011-12-16'
# }

result = es.update(index='news',doc_type='politics', id=1,body=data)
print(result)
