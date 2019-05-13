from enum import Enum, unique
from enum import IntEnum
'''
枚举类型 不能重复          Attempted to reuse key: 'YELLOW'
vip.YELLOW 不能进行修改   Cannot reassign members.
枚举其实就是单例模式的实现
'''
'''
@unique   这个装饰器的作用是使enum不能有重复的value值 也就是不能别名
'''
class vip3(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 3
    BLACK = 4

@unique    #这个装饰器的作用是使enum不能有重复的value值 也就是不能别名
class vip(Enum):
    YELLOW = 1
    # YELLOW_ALISA = 1    #YELLOW的别名
    GREEN = 2
    RED = 3
    BLACK = 4

class vip2(IntEnum):    #里面的value对应的值 只能是int类型  若为str则会报错
    YELLOW = 1
    GREEN = 2
    # PUROLE ='SSS'     #invalid literal for int() with base 10: 'SSS'
    RED = 3
    BLACK = 4
# print(vip.BLACK)


for value in vip:
    print(value)    #只会打印YELLOW 不会打印YELLOW_ALISA

for value in vip.__members__:   #会打印所有存在enum的元素，包括别名元素
    print(value)


value = 1    #若从数据库取出对应的值  通过className(value)的到具体的枚举标签
print(vip(value))  #vip(value)    <enum 'vip'>

print(type(vip(value)))

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    '''
    将一个类固定的属性类别   从字符串改为枚举类， 可以更好的限定属性的值，并且不会写错
    固定长度的默认字符串常量  可以用枚举类进行实现
    '''
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

print(Gender(Gender.Male))