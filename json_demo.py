import json
import requests


# address = 'https://api.avatardata.cn/HistoryToday/LookUp?key=ccfde50a9f30475b963d2b8bf7266778&yue={yue}&ri={day}}&type=1&page=1&rows=20'

# print('please input you want to get date lile this "12-04" ')
# want_get_date = input()

# yue,day = tuple(want_get_date.split('-'))

# address = address.format(yue=yue,day=day)

# response = requests.get(address)

# json_str = response.text()

# print(json_str)
json_str = '{"total":22,"result":[{"year":2002,"month":12,"day":6,"title":"我科学家发现核反应堆中微子消失现象","type":1},{"year":2001,"month":12,"day":6,"title":"广西壮族自治区常务副主席刘知炳被查处","type":1},{"year":2001,"month":12,"day":6,"title":"中国航油在新加坡成功上市","type":1},{"year":1999,"month":12,"day":6,"title":"南疆铁路全线开通运营","type":1},{"year":1998,"month":12,"day":6,"title":"查韦斯当选委内瑞拉总统","type":1},{"year":1997,"month":12,"day":6,"title":"俄发生重大坠机事故","type":1},{"year":1997,"month":12,"day":6,"title":"我国早期女企业家董竹君逝世","type":1},{"year":1995,"month":12,"day":6,"title":"中俄朝韩蒙签署图们江地区开发协定","type":1},{"year":1992,"month":12,"day":6,"title":"印度爆发教族骚乱  造成1100多人死亡  4000多人受伤","type":1},{"year":1986,"month":12,"day":6,"title":"泥沙学家钱宁逝世","type":1},{"year":1985,"month":12,"day":6,"title":"我军卓越的政治工作者谭冠三逝世","type":1},{"year":1985,"month":12,"day":6,"title":"三北防护林体系一期工程结束","type":1},{"year":1984,"month":12,"day":6,"title":"中国新闻学会成立","type":1},{"year":1984,"month":12,"day":6,"title":"英文版《邓小平文集》在伦敦出版","type":1},{"year":1979,"month":12,"day":6,"title":"西单“民主墙”禁贴大字报","type":1},{"year":1957,"month":12,"day":6,"title":"美国实验性人造卫星爆炸","type":1},{"year":1938,"month":12,"day":6,"title":"周恩来同蒋介石商谈两党合作","type":1},{"year":1926,"month":12,"day":6,"title":"法国画家莫奈逝世","type":1},{"year":1922,"month":12,"day":6,"title":"爱尔兰自由邦成立","type":1},{"year":1917,"month":12,"day":6,"title":"芬兰宣布脱离俄国独立","type":1}],"error_code":0,"reason":"Succes"}'
student = json.loads(json_str)    #反序列化为一个字典
print(student)
print(type(student))

for data in student['result']:
    print('%s-%s-%s:%s'%(data['year'],data['month'],data['day'],data['title']))


json_dict = [
                {'name':'make','age':24,'flag':True},
                {'name':'tubu','age':25}
            ]

json_str = json.dumps(json_dict)  #  序列化为json字符串

print(json_str)

