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


l4_to_l6 = 12 #消耗12颗4级石头 一共13颗4级石头
l4_to_l6_gold = 19.75 #同时消耗19.75金
l4_to_l6_vit = 10 #同时消耗10点体力

gold_cost = 0
diamond_cost = 0
vit_cost = 0

l1_get = 0
l3_get = 0
l4_get = 0
l6_get = 0

def get_l1_stone():
    global gold_cost
    global diamond_cost
    global l1_get

    gold_cost += 0.75
    diamond_cost += 8
    l1_get += 1
    # print('金消耗：%s, 钻石消耗：%s, 一级五行石库存：%s'%(gold_cost, diamond_cost,l1_get))

def get_l3_stone():
    global l1_get
    global diamond_cost
    global vit_cost
    global gold_cost
    global l3_get
    
    while l1_get < 13:
        get_l1_stone()
    l1_get -= 13
    gold_cost += 0.39
    vit_cost  += 10
    l3_get += 1
    # print('金消耗：%s, 钻石消耗：%s,体力消耗：%s, 一级五行石库存：%s，三级五行石库存：%s'%(gold_cost, diamond_cost,vit_cost,l1_get,l3_get))
    

def get_l4_stone():
    global l1_get
    global diamond_cost
    global vit_cost
    global gold_cost
    global l3_get
    global l4_get

    rate = random.random()

    if rate > 0.4878:
        while l1_get < 16:
            get_l1_stone()
        l1_get -= 16
        while l3_get < 1:
            get_l3_stone()
        l3_get -= 1
        gold_cost += 0.897
    else:
        l1_get -= 16
        while l1_get < 0:
            get_l1_stone()
        l3_get -= 1
        while l3_get < 0:
            get_l3_stone()
        gold_cost += 0.897
        vit_cost += 10
        l4_get += 1
    # print('金：%s, 钻石：%s,体力：%s, 一级五行石：%s，三级五行石：%s,四级五行石：%s'%(gold_cost, diamond_cost,vit_cost,l1_get,l3_get,l4_get))


def get_l6_stone():
    global l1_get
    global diamond_cost
    global vit_cost
    global gold_cost
    global l3_get
    global l4_get
    global l6_get

    l4_get -= 13
    while l4_get < 0:
        get_l4_stone()
    gold_cost += 19.75
    vit_cost += 10
    l6_get += 1
    print('金：%s, 钻石：%s,体力：%s, 一级：%s，三级：%s,四级：%s,六级：%s'%(gold_cost, diamond_cost,vit_cost,l1_get,l3_get,l4_get,l6_get))



while l6_get < 5:
    get_l6_stone()


avg_cost = (gold_cost + 0.05*diamond_cost + vit_cost) / 5


if avg_cost > 750:
    print('平均花费：%s,所以买划算'%avg_cost)
else:
    print('平均花费：%s,所以合成划算'%avg_cost)
    
