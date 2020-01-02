# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:59
# @Author  : dengwenxing
# @Software: PyCharm
import faker
from collections import OrderedDict
import time
from datetime import datetime, date

f = faker.Faker(locale='zh_CN')


'''类似的字段，调用相同的函数,前者为主函数，后者的字段都调用前者的标准函数'''

like_link_func = OrderedDict()
like_link_func["time"] = ["qfsj","ddsj"]
like_link_func["address"] = ["xxdz","hjd"]
like_link_func["sfzh"] = ["start_person","end_person"]
like_link_func["phone"] = ["start_phone","end_phone"]


local_info = locals()
def initFunc():
    funcs = OrderedDict()
    for fname in local_info:
        if fname.startswith("get"):
            funcs[fname[4:]] = local_info[fname]
    for key in like_link_func:
        for name in like_link_func[key]:
            funcs[name] = funcs[key]
    return funcs

''' 以下为标准函数每种类型应该都会有一个 '''
def get_address():
    '''得到地址相关信息'''
    return f.address()
def get_xm():
    return f.name()
def get_phone():
    return f.phone_number()
def get_sfzh():
    return f.ssn()
def get_province():
    return f.province()
def get_city():
    return f.city()
def get_gj():
    return f.country()

def get_start_time(start_date='-5y',end_date = '-2y'):
    return int(time.mktime(f.date_between(start_date=start_date,end_date=end_date).timetuple()))

def get_end_time(start_date='-2y',end_date = 'today'):
    return int(time.mktime(f.date_between(start_date=start_date, end_date=end_date).timetuple()))

def get_time(start_date='-4y',end_date = 'today'):
    return int(time.mktime(f.date_between(start_date=start_date, end_date=end_date).timetuple()))


if __name__ == '__main__':
    pass


