'''
map reduce 深刻理解案例
1、map 方法返回的值是一个map，其内部的值为，传入的方法依次对原列表元素作用后生成的值
2、map可以传入多个参数，map(lambda x,y:x+y, list_x,list_y),可变参数，列表的个数 取决于lamdba的参数个数
3、reduce方法出入的值为一个列表，依次对列表里的两两元素进行运算，结果和下一个元素继续进行此项运算，最后返回值根据项目需要而定
'''
from functools import reduce
from collections import defaultdict,OrderedDict

list1 = [1,2,3,4]
list2 = [5,6,7,8]

list3 = [list1, list2]

res = map(lambda x: x ** 2,list2)

print(type(res))

# for value in res:
#     print(value)

res = reduce(lambda x,y: x * 10 + y,list1)
print(res)

scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def reducer(accumulator , value):
    # sum = accumulator['age'] + value['age']   错误示范   最后一次accumulator为int类型 没有['age']方法 执行会报错
    sum = accumulator + value['age'] 
    return sum
# total_age = reduce(reducer, scientists) 错误示范  没有给定一个初始值
total_age = reduce(reducer, scientists, 0)
total_age2 = sum(data['age'] for data in scientists)  #更简单的完成方式
print(total_age, total_age2)

def group_by_gender(accumulator, value):
    accumulator[value['gender']].append(value['name'])
    return accumulator

list4 = [u'瞎子',u'瑞文','鳄鱼']
list5 = [u'盲僧',u'放逐之刃',u'荒漠之主']

dic = OrderedDict(zip(list4,list5))


total_gender = reduce(group_by_gender, scientists, defaultdict(list))
print(total_gender)
print(dic)

sorted_scientists = sorted(scientists, key=lambda x : x['name'])
print(sorted_scientists)

tuple1 = [(1,2,3,4)]
tuple1.append((5,6,7,8))
print(tuple1)