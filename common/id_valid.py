# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 20:13
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : id_valid.py
# @Software: PyCharm

from id_validator import validator

def sfzh_test():
    res = validator.get_info('511622199310226471')
    print(res)

if __name__ == "__main__":
    sfzh_test()