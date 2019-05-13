
class Student():
    
    sum = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        print(name)
        print(age)
        Student.sum += 3
        # print(Student.sum)

    def do_homework(self):
        print('homework')

student = Student('鸡小萌', 22)
print(student.name)
print(Student.sum)


'''
__slots__对类的属性进行限制，在使用类对其进行属性绑定时 可对其限制限制
'''

class Student1(object):
    __slots__ = ['name','age']     #限制Student1 的属性只能为 name age
    pass

s1 = Student1()
s1.name = 'make'
# s1.score = 99       #若超出限制 报错  AttributeError: 'Student1' object has no attribute 'score'



class Screen(object):
    '''
    width height 为@property  @width.setter 所修饰的  可读可改变的属性
    resolution 为@property   所修饰的只读属性
    '''
    @property
    def width(self):
        return self._width
   
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        self._width = value

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return 786432


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



class custom(object):
    '''
    定制类    即自己改写class的内部方法
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):  #在答应我们的类时，定制我们的返回结果
        return 'name:'+self.name + ' -- age:' + str(self.age)
    __repr__ = __str__

# print(dir(custom))
c = custom('make',28)
print(c)

class Fib(object):
    '''
    将一个类修改为  可迭代的对象
    并使其可以支持  索引查找  切片操作
    '''

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    def __getitem__(self,n):
        if isinstance(n,int):
            for i in range(n):
                self.a,self.b = self.b,self.a + self.b
            return self.b
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            L = []
            a,b = 1,1
            for x in range(stop):
                if x >= start:
                #     L.append(self.b)
                # self.a,self.b = self.b,self.a + self.b    这两种写法都可以
                    L.append(a)
                a,b = b,a+b
            return L
fib = Fib()
print(fib[1:10])



class attr(object):
    '''
    若不自己实现 __getattr__ 方法  调用a.score 就会报错 
    AttributeError: 'attr' object has no attribute 'score'
    '''

    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __getattr__(self,attr):
    #     if attr == 'score':
    #         return 90

a = attr('make',24)
print(a.name)
print(a.age)
# print(a.score)    #若不自己实现 __getattr__ 方法  调用a.score 就会报错 AttributeError: 'attr' object has no attribute 'score'

class attr2(object):
    '''
    可以实现动态的调用，不用一个个去定义
    '''
    def __init__(self,name,age,path=''):
       self.name = name
       self.age = age
       self._path = path
    def __getattr__(self,path):
        return attr2('default',0,'%s%s'%(self._path,path))

    def __str__(self):
        return self._path

a2 = attr2('make',24)

print(a2.status.user.timeline.list)