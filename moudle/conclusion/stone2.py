l1_value = 0.75
l1_diamond = 0.8
#一级宝石需要的金 one_value
def goone():
    one_value = l1_value + l1_diamond * 0.05
    return one_value 

# 升级3级石头需要的金 three_value

def gothree():
    three_value = goone() * 12 + 0.39 + 10
    return three_value

#升级4级宝石需要的金four_value

def gofour():
    four_success = gothree() + goone()*16 + 0.897 + 10#成功消耗的金
    four_fail = gothree() + goone()*16 + 0.897 #失败消耗的金

    four_values = (four_success * 0.4878 + four_fail * 0.5122)/0.4878 #平均四级宝石消耗 = （成功消耗*成功率+失败消耗*成功率）/成功率
    return four_values

#升级6级宝石需要的金 six_value

def gosix():
    six_value = gofour()*12+19.75+10
    print(six_value)
    return six_value
def result():
    if gosix()>750:
        print("不划算")
    else:
        print("划算")

result()