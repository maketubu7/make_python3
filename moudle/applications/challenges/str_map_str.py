''' 将下面的 字符串 转换一串有意义的字符串 '''
import string
text = ''' g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''


def my_func(text):
    ''' 对于转换后的ascii码 超过了z 则继续 从z-a开始进行轮询 '''
    res = ''
    for o in text:
        if ord(o) >= ord('a') and ord(o) <= ord('z'):
            # 超过的ascii码的处理
            res += chr((ord(o) + 2- ord('a')) % 26 + ord('a'))
        else:
            res += o

    return res

def my_func_2(text):
    '''  str.maketrans(str1, str2) 返回为str1 => str2 的映射表 str可以调用 text.translate(table)来对字符串进行相应的转换 '''
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    res = text.translate(table)
    return res

if __name__ == '__main__':
    res1 = my_func(text)
    res2 = my_func_2(text)
    print(res1)
    print(res2)