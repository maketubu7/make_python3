
# @Time    : 2019/12/31 14:02
# @Author  : dengwenxing
# @Software: PyCharm

s = '\xE9\xAB\x98\xE6\x9E\x97'
ss = s.encode('raw_unicode_escape')
print(ss)  # 结果：b'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
sss = ss.decode()
print(sss)