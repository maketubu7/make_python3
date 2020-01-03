# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:59
# @Author  : dengwenxing
# @Software: PyCharm
import faker
from collections import OrderedDict
import time
from datetime import datetime, date
from random import randint

f = faker.Faker(locale='zh_CN')


'''类似的字段，调用相同的函数,前者为主函数，后者的字段都调用前者的标准函数'''

like_link_func = OrderedDict()
like_link_func["start_time"] = ["clrq"]
like_link_func["qfsj"] = ["fcsj"]
like_link_func["ddsj"] = ["dzsj"]
like_link_func["address"] = ["xxdz","hjd","qydz"]
like_link_func["sfzh"] = ["start_person","end_person"]
like_link_func["phone"] = ["start_phone","end_phone"]
like_link_func["sfd"] = ["mdd","sfz","zdz"]


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
get_address = lambda : f.address().split(" ")[0]
get_xm = lambda : f.name()
get_phone = lambda : f.phone_number()
get_sfzh= lambda : f.ssn()
get_province = lambda : f.province()
get_city= lambda : f.city()
get_gj= lambda : f.country()
get_sfd = lambda : f.city()
get_companyname = lambda :f.company()
#企业类型
get_qyxz = lambda : f.company_suffix()
get_companyid = lambda : f.md5()

def get_start_time(start_date='-5y',end_date = '-2y'):
    return int(time.mktime(f.date_between(start_date=start_date,end_date=end_date).timetuple()))

def get_end_time(start_date='-2y',end_date = 'today'):
    return int(time.mktime(f.date_between(start_date=start_date, end_date=end_date).timetuple()))

def get_time(start_date='-4y',end_date = 'today'):
    return int(time.mktime(f.date_between(start_date=start_date, end_date=end_date).timetuple()))

def get_hbh():
    hkgsdm = ["3U","TV","MU","CA","MF","CZ","CJ","WH","SC","SZ","HR","WC","MD","HK"]
    suffix = lambda : f.numerify()
    return hkgsdm[randint(0, len(hkgsdm)-1)] + suffix()

def get_hcbc():
    hcdm = ["G", "C", "D", "K", "T","Z","Y","A","L","H","E","N","S","R"]
    suffix = lambda: f.numerify()
    return hcdm[randint(0, len(hcdm)-1)] + suffix()

def get_qfsj():
    '''出发时间'''
    return int(time.mktime(f.date_between(start_date='-3d', end_date='-2d').timetuple()))

def get_ddsj():
    '''到达时间'''
    return int(time.mktime(f.date_between(start_date='today',end_date='today').timetuple()))


if __name__ == '__main__':
    print(f.company())
    print(f.company_suffix())
    print(f.bs())


