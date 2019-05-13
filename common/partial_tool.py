'''

偏函数  用于创建快捷的默认函数
int(str,base=scale)  将字符串转换为指定的进制数 base为默认参数指定对应的进制

'''

__author__ = 'make'

import functools

int2 = functools.partial(int, base=2)


print(int2('10'))