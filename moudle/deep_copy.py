import copy
a = [1,2,['aa','bb']]
d = a
b = a.copy()
c = copy.deepcopy(a)

a[0] = 2
a[2].append('c')

print(a)
print(d)
print(b)
print(c)

class signtlon():
    _instance = None

    def __new__(cls, *args, **kwwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

a = signtlon('make',20)
b = signtlon('tubu',30)

print(a)
print(b)