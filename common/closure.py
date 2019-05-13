
'''
闭包   函数+环境变量
若在定义函数返回的时候，没有定义环境变量，则无法形成闭包，调用返回的函数，会去找上一级作用域的变量，值就会改变
'''

def pures(): 
    a,b,c = 4,33,2
    def pure(x):
        return a*x*x + b*x + c

    return pure


def pures2(): 
    def pure(x):
        return a*x*x + b*x + c

    return pure

a,b,c = 1,1,1    #即时在这里改变了a,b,c,的值，但是函数的返回值仍然是不变的，在定义时就已经随环境变量定义好了，不会改变
f = pures()
f2 = pures2()
print(f(2))
print(f.__closure__)   #这个对象里保存了我们的环境变量
print(f.__closure__[0].cell_contents)   #1
print(f.__closure__[1].cell_contents)   #2
print(f.__closure__[2].cell_contents)   #3
print(f2(2)) 



def f1():
    a = 10

    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()

'''
闭包经典误区
'''

def f3():
    a = 4

    def f4():
        a = 20
        return a
    return f4

f = f3()
print(f.__closure__)       # 这里的__closure__ 返回的值是None  说明并没有现场的环境变量被保存返回， 原因是变量在函数内部，不是外部变量

def f5():
    a = 4
    def f6():
        # a = 20           #不传入内部变量  传入外部变量但不是全局变量， 就是一个完美的闭包  可以携带现场环境变量返回
        return a
    return f6

f = f5()
print(f.__closure__)


'''
给个问题   用闭包解决一下   计算  旅行者的位置  每调用一次  返回当前的位置信息
主要思路   让每一次的返回都保存上一次的计算结果
'''
location = 0
def get_location(zero):
    def get_index(x):
        nonlocal zero     #申明为非环境变量   否则报错   local variable 'zero' referenced before assignment
        zero = zero + x
        new_pos = zero
        return new_pos
    # location += get_index(x)
    return get_index


get_x = get_location(location)

print(get_x(3))
print(get_x(2))
print(get_x(7))
print(get_x(9))







