'''
爬虫分析
'''
import requests
import re
class Spider():
    url = 'https://www.panda.tv/cate/lol'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    root_regex = '<div class="video-info">(.+?)</div>'
    name_regex = '<span class="video-nickname" title="(\S+)">'
    num_regex = '<i class="ricon ricon-eye"></i>(\S+)</span>'

    def __fetch_content(self):
        response = requests.get(Spider.url,headers=Spider.header)
        if response.status_code != 200:
            return None
        else:
            html = str(response.content,encoding='utf-8')
            return html

    def __analysis(self, html):
        root_html = re.findall(self.root_regex,html, re.S)
        anchors = []
        for html in root_html:
            name = re.findall(self.name_regex,html)
            num = re.findall(self.num_regex,html)            
            anchor = {'name':name,'num':num}
            anchors.append(anchor)
        return anchors
    def __refine(self,anchors):
        func = lambda anchor: {'name':anchor['name'][0].strip(), 'num':anchor['num'][0].strip()}
        data = map(func,anchors)
        return list(data)

    def __sorted(self,data):
        def clean(key):
            if u'万' in key:
                key = float(key.strip('万')) * 10000
            else:
                key = int(key)
            return key
        func = lambda anchor: clean(anchor['num'])
        res = sorted(data, key=func,reverse=True)
        return res
    def __show(self,res):
        # req = [x for x in range(0,len(res))]
        i = 1
        for anchor in res:
            print('rank%s: %s %s'%(i,anchor['name'],anchor['num']))
            i += 1
    def go(self):
        html = self.__fetch_content()
        anchors = self.__analysis(html)
        data = self.__refine(anchors)
        res = self.__sorted(data)
        self.__show(res)

if __name__ == "__main__":
    spider = Spider()
    spider.go()