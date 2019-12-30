# -*- coding:utf-8 -*-
# @Time    : 2019/12/27 15:39
# @Author  : dengwenxing
# @Software: PyCharm

from faker import Faker
from random import randint
f = Faker(locale='zh_CN')

def getFakerPerson(init_num):
    '''

    :param num: 默认生成1000个人
    :return:
    '''
    index = 0
    xms = []
    address = []
    ages = []
    while index < init_num:
        xm = f.name()
        dz = f.address()
        age = randint(10,89)
        xms.append(xm)
        address.append(dz)
        ages.append(age)
        index += 1
    return {"name":xms,"address":address,"age":ages}


def getFakerCall(init_num):
    index = 0
    start_phones = []
    end_phones = []
    nums = []
    while index < init_num:
        start_phone = f.phone_number()
        if index > 10 and index % randint(2,5) == 0:
            end_phone = start_phones[int(index/2)]
        else:
            end_phone = f.phone_number()
        num = randint(100,999)
        start_phones.append(start_phone)
        end_phones.append(end_phone)
        nums.append(num)
        index += 1
    return {"start_phone": start_phones, "end_phone": end_phones, "num": nums}

if __name__ == '__main__':
    result = getFakerCall(100)
    start = set(result["start_phone"])
    end = set(result["end_phone"])
    print(len(start & end))




