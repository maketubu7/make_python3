#encoding=utf8
import threading
import time
import functools
from functools import reduce
import signal
'''
1、装饰器    python的高级知识，对实践有巨大作用  
2、为了解决在开闭原则下的需求变更问题，对方法和类不进行修改，对修改关闭，对扩展开放
3、带参数的装饰器，相当于在装饰器的内部再返回一个装饰器，内部的装饰器接受函数的参数，
4、一个函数可以有多个装饰器，共同对其进行作用
'''

def decorator(func):
    def wrapper(*args, **kwargs):    #这样来设计表示  可以对各种参数形式的函数进行装饰
        print(time.time())
        func(*args, **kwargs)
    
    return wrapper

@decorator    #装饰器最大的优点就是给与的这个语法糖@,如果没有这个语法糖，那么简洁也无从谈起
def f(name):
    print('This is a function ' + name)


@decorator    #装饰器最大的优点就是给与的这个语法糖@,如果没有这个语法糖，那么简洁也无从谈起
def f1(name1, name2):
    print('This is a function ' + name1)
    print('This is a function ' + name2)


@decorator    #装饰器最大的优点就是给与的这个语法糖@,如果没有这个语法糖，那么简洁也无从谈起
def f2(name1, name2, **kwargs):
    print('This is a function ' + name1)
    print('This is a function ' + name2)
    print(kwargs)

f('name')
f1('name1', 'name2')
f2('name1', 'name2',a=1,b=2,c=3)

'''
带参数的装饰器
'''
def log(case):
    def wrapper(func):
        def increase(*args, **kwargs):
            print(time.time())
            print(case)
            return func(*args, **kwargs)
        return increase
    return wrapper

def log_v2(case):
    def wrapper(func):
        @functools.wraps(func)    #如果没有这样的装饰器，内置的一些变量比如__name__ 就会发生改变， 这里就会把increase的相关内置变量，变为和func（原来的函数）的内置变量为一样的
        def increase(*args, **kwargs):
            print(time.time())
            print(case)
            return func(*args, **kwargs)
        return increase
    return wrapper



@log('make tubu ')
def f4(data1, data2):
    print(data1 + data2)

f4('hello','hei hei')

#函数运行时间装饰器
def time_count(func):
    def wrapper(*args, **kwaggs):
        start_time = time.time()
        result =  func(*args, **kwaggs)    #有函数返回值的函数，提前对返回值进行return 在进行装饰器的定义
        print('used time:'+ str(time.time() - start_time))
        return result
    return wrapper


@time_count
def f5(list_a):
    res = reduce(lambda x,y:x + y,list_a)
    return res

res = f5([x for x in range(0,10000000)])
print(res)

def time_limited(timer):
    '''
    一个规定函数执行时间的装饰器,windows 下也可使用的时间限制装饰器
    :param timer:
    :return:
    '''
    def wrapper(func):
        def __wrapper(*args, **kwargs):
            start_time = time.time()
            # 通过设置守护线程强制规定函数的运行时间
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)
            t.start()
            time.sleep(timer)
            if t.is_alive():
                # 若在规定的运行时间未结束守护进程，则主动抛出异常
                raise Exception('Function execution timeout')  # print time.time()-start_time
        return __wrapper
    return wrapper

def time_limited2(num):
    def wrapper(func):
        def handle(signum,frame):
            raise RuntimeError
        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM,handle)
                signal.alarm(num)
                r = func(*args, **kwargs)
                signal.alarm(0)
                return r
            except RuntimeError as e:
                pass
        return to_do
    return wrapper

print(dir(signal))
