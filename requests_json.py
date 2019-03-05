import json
import requests
import os
import datetime,time
import re
import random

def get_news(key):
    address = 'https://api.avatardata.cn/HistoryToday/LookUp?key=ccfde50a9f30475b963d2b8bf7266778&yue={yue}&ri={day}&type=1&page=1&rows=20'

#     print('please input you want to get date lile this "12-04" ')
#     want_get_date = input()
    want_get_date = key

    yue,day = tuple(want_get_date.split('-'))

    address = address.format(yue=yue,day=day)

    response = requests.get(address)
    json_str = response.text

    news = json.loads(json_str)

    for data in news['result']:
        print('%s-%s-%s:%s'%(data['year'],data['month'],data['day'],data['title']))
def get_laugh(key):
    address = 'http://api.avatardata.cn/Joke/QueryJokeByTime?key=bbf74bdfcd2e44729a7b257cdfc6eeaf&page=2&rows=20&sort=asc&time={time_str}&format=true'
#     print('please input you want to get date lile this "2018-12-04" ')        
#     want_get_date = input()
    want_get_date = key

    date = time.strptime(want_get_date,'%Y-%m-%d')
    time_str = int(time.mktime(date))

    address = address.format(time_str=str(time_str))
    response = requests.get(address)
    json_str = response.text

    laughs = json.loads(json_str)
    for data in laughs['result']:
        content = data['content']
        print('%s:%s'%(data['updatetime'],clean_content(content,'\W{2,4}')))

def clean_content(data,regex):
    
    def convert(value):
        matched = value.group()
        pass
    clean_contents = re.sub(regex,convert,data)
    return clean_contents

def get_famous(key):
    address = 'http://api.avatardata.cn/MingRenMingYan/LookUp?key=77d981fa31f94e708d96ec04f2a48990&keyword={keyword}&page=1&rows=20&format=true'
#     print('please input you want to get keyword this "努力" ')
#     keyword = input()
    keyword = key

    address = address.format(keyword=keyword)
    response = requests.get(address)

    json_str = response.text

    fanouss = json.loads(json_str)

    for data in fanouss['result']:
        print('%s:%s'%(data['famous_name'],data['famous_saying']))

def get_dream(key):
    address = 'http://api.avatardata.cn/ZhouGongJieMeng/LookUp?key=33970163823a458c8466545dc3d7633c&keyword={keyword}'
#     print('please input you want to get keyword this "努力" ')
#     keyword = input()
    keyword = key

    address = address.format(keyword=keyword)
    response = requests.get(address)

    json_str = response.text

    dreams = json.loads(json_str)

    for data in dreams['result']:
        content = data['content']
        print('%s:%s'%(data['title'],clean_content(content,'<.{3,4}>')))

month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
day_list = [x for x in range(1,30)]
year_list = [2018, 2017, 2016, 2015]
keywords = ['努力','天才','浪漫','汗水','爱情','现实','积累','理想','自由','光芒','向往','生命']
drean_keywords = ['梦见蛇','梦见大海','梦见妈妈','梦见鬼','梦见黄金','梦见死人','梦见很多钱','梦见自杀',]

mon_day = str(random.sample(month_list,1)[0]) + '-' + str(random.sample(day_list,1)[0])
year_mon_day = str(random.sample(year_list,1)[0]) + '-' + str(random.sample(month_list,1)[0]) + '-' + str(random.sample(day_list,1)[0])
keyword = random.sample(keywords,1)[0]
dream_keyword = random.sample(drean_keywords,1)[0]
# print('~~~~~~~~~~~~~ %s 历史上的今天 ~~~~~~~~~~~~~~~~'%mon_day)
# get_news(mon_day)
print('~~~~~~~~~~~~~ %s 之前的笑话 ~~~~~~~~~~~~~~~~'%year_mon_day)
get_laugh(year_mon_day)
print('~~~~~~~~~~~~~ %s 名人名言 ~~~~~~~~~~~~~~~~'%keyword)
get_famous(keyword)
print('~~~~~~~~~~~~~ %s 周公解梦 ~~~~~~~~~~~~~~~~'%dream_keyword)
get_dream(dream_keyword)