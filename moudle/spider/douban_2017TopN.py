'''
抓取豆瓣2017 各地区电影榜单
1、找到数据入口  https://movie.douban.com/annual/2017
2、分析返回的html
'''

import requests
import re

class Spider():
    url = 'https://movie.douban.com/subject/26606242/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    
    info_root_regex = 'div id="info">(.+)</div>'
    info_director_regex = 'directedBy">(\w+)</a>'
    info_editers_regex = 'href="/celebrity/\d+/">(\w+)</a>'
    info_actors_regex = 'rel="v:starring">(\w+?)</a>'

    info_introduce_regex = '<span property="v:summary" class="">(.+?)</span>'


    short_root_regex = '<div class="comment">(.+?)</div>'
    short_content_regex = '<span class="short">(.+)</span>'
    def __fetch_content(self,url):
        response = requests.get(Spider.url, headers=Spider.header)

        if response.status_code != 200:
            return None
        else:
            return str(response.content,encoding='utf-8')

    def __analysis_info(self,html):
        short_anchors = re.findall(Spider.short_root_regex, html, re.S)
        anchors = []
        for short in short_anchors:
            anchor = re.findall(Spider.short_content_regex,short, re.S)
            if len(anchor) == 1:
                anchors.append(anchor[0])

        info_anchors = re.findall(Spider.info_root_regex,html,re.S)[0]
        directors = re.findall(Spider.info_director_regex, info_anchors)
        editers = re.findall(Spider.info_editers_regex, info_anchors)
        actors= re.findall(Spider.info_actors_regex, info_anchors)
        introduce = re.findall(Spider.info_introduce_regex,html, re.S)[0].strip()
        info = {'director':directors[0],'editers':(','.join(editers)),'actors':(','.join(actors)),'introduce':introduce,'short_top5':('|| '.join(anchors))}
        return info
    
    def __analysis_short(self,html):
        short_anchors = re.findall(Spider.short_root_regex, html, re.S)
        anchors = []
        for short in short_anchors:
            anchor = re.findall(Spider.short_content_regex,short, re.S)
            if len(anchor) == 1:
                anchors.append(anchor)
        return anchors
    
    # def __refine(self,anchors):
        
    
    def go(self):
        html = self.__fetch_content(Spider.url)
        # short_anchors = self.__analysis_short(html)
        # self.__refine(short_anchors)
        return self.__analysis_info(html)
        

if __name__ == "__main__":
    spider = Spider()
    res = spider.go()
    print(res)

