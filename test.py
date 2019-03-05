'''make tubu test
'''
import moudle.inlay
import sys

print(dir(sys))

print('~~~~~~~~~~~~test.py~~~~~~~~~~~~~~~')
print('package:' + (__package__ or "该模块不属于任何模块"))
print("name:"  + __name__)
print('doc: ' + __doc__)
print('file:'  + __file__)