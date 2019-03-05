# 乘数大于1 仅包含数字 字母 下划线 且乘法后不超过20个字符  默认驻留
# 乘数大于1 其他字符 无论长度 不驻留
a = 'asdasasdas'
b = 'asdas'*2
print('仅包含数字 字母 下划线 默认驻留 ')
print(a is b)

# 乘数为1 仅包含数字 字母 下划线 默认驻留
# 乘数为1 其他字符 原长度为1 默认驻留
# 乘数为1 其他字符 原长度>1 不驻留
a = 'asdasdasdasdasfasfasfasfafa'
b = a*1
print('仅包含数字 字母 下划线 默认驻留 ')
print(a is b)

a = '#'
b= a*1
print('其他字符 原长度=1 默认驻留 ')
print(a is b)

a = '##'
b= a*1
print('其他字符 原长度>1 不驻留 ')
print(a is b)