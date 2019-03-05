'''
划算还是不划算?  自己合成还是系统购买
一颗6级五行石 = 750金
1颗钻石 = 0.05金
1点体力 = 1.00金
'''
import random

l1_value = 0.75  #一颗一级石头 0.75金
l1_value_diamond = 8 #同时还需8颗钻石


l1_to_l3 = 12 #一级到三级 消耗12颗一级石头   共消耗13颗
l1_to_l3_gold = 0.39 #合成的同时需要0.39金
l1_to_l3_vit = 10 #合成的同时需要10体力


l3_to_l4 = 16 #消耗1颗三级 + 16颗一级
l3_to_l4_gold = 0.897 #同时消耗0.897金
l3_to_l4_vit = 10 #同时消耗10点体力
l3_to_l4__rate = 0.4878 #成功的概率 若失败则金和石头扣除，体力值返回


l4_to_l6 = 13 #消耗12颗4级石头 一共13颗4级石头
l4_to_l6_gold = 19.75 #同时消耗19.75金
l4_to_l6_vit = 10 #同时消耗10点体力

def get_l1_stone(num):
    return num * (l1_value + l1_value_diamond * 0.05)


def get_l3_stone(num):
    return num * (get_l1_stone(13) + 0.39 + 10)

def get_l4_stone(num):
    sum = 0
    i = 0
    while i < num:
        rate = random.random()
        if rate > l3_to_l4__rate:
            sum += get_l1_stone(16) + get_l3_stone(1) + 0.897
        else:
            sum += get_l1_stone(16) + get_l3_stone(1) + 0.897 + 10
            i += 1
    return sum

def get_l6_stone(num):
    return num * (get_l4_stone(13) + 19.75 + 10)


def get_avg_gold(num):
    sum = get_l6_stone(num)
    avg_gold = round(sum / num)

    if avg_gold > 750:
        print('avg_gold:%s, 直接买划算'%avg_gold)
    else:
        print('avg_gold:%s,自己合成划算'%avg_gold)


get_avg_gold(10)
