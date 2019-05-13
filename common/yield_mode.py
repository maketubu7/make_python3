'''
yield 生成器
只要函数里包含了 yield关键字， 该函数就会变成一个生成器
生成器是一个迭代器，但迭代器不一定是生成器
'''

def func():
    for i in range(10):
        print('step'+str(i))
        yield i

k1 = [i for i in range(10)]     #列表生成器   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k = (i for i in range(10))      #生成器   <generator object <genexpr> at 0x0105D870>
print(k)
print(k1) 
# print(next(k))       #每一个next 抛出一个值，并保持当前的状态，为下一次返回做准备
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))


# f = func()
# while True:       #若迭代完成 则会抛出StopIteration的错误 并退出
#     k = next(f)  
#     print(k)  

'''
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
1 6   15   20  15  6  1
用yield 输出 杨辉三角的下一行的值   用列表表示
'''

# def triangle():
#     i = 1
#     l = 1
#     while True:
#         if l == 1:
#             yield list(1)
#             l +=1
#             i += 1
#         if l == 2:
#             yield list(1,1)
#             i += 1
#             l += 1
#         else:
#             res = []
#             for k in rangge(l):
#                 v = 1
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
i = 1 
k = triangles()       
while i < 10:
    i += 1
    v = next(k)
    print(v)


'''
Fibonacci  斐波那契数列 1 1 2 3 5 8 13 。。。
'''

def fib(n):
        i, x ,y = 0, 0, 1
        while i < n:
                print(y)
                x,y=y,x+y
                i += 1
        return 'done'

fib(6)

'''
斐波拉契数列 使用yield实现，每次保存一个结果
'''
def fib2(n):
        i, x ,y = 0, 0, 1
        while i < n:
                yield y
                x,y=y,x+y
                i += 1
        return 'done'


f = fib2(10)

