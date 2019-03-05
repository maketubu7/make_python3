from collections import OrderedDict

x = [str(x) for x in range(1,10)]
y = [x for x in range(1,10)]

z = zip(x,y)
z1 = ','.join(x)
z2 = OrderedDict(z)
print(z1)
print(type(z))


for k,v in z2.items():
    print(k,v)