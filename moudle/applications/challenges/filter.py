import requests
import re
import string
''' 对源代码的 '''
response = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
response2 = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

text = response.text
text2 = response2.text

regex = '<!--\nfind rare characters in the mess below:\n-->\n\n<!--(.+)-->'
regex2 = '<!--(.+)-->'
char_regex = '[A-Za-z]'
char_regex2 = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
result = re.findall(regex, text, re.S)[0]
result2 = re.findall(regex2, text2, re.S)[0]


chars1 = ''.join(re.findall(char_regex, result))

#filter 函数 返回filter(func, resource)  依次迭代resource，返回func为true的值， 结果为一个filter对象 需转为list对象
chars2 = ''.join(list(filter(lambda x: x in string.ascii_letters, result)))
print(chars1,chars2)

# 稀有性原则 对每个字符的平均出现次数 进行判断
result = result.strip().replace('\n','')

occ = {}

for c in result:
    occ[c] = occ.get(c,0) + 1
    avg = len(result) / len(occ)
# 对平均出现次数 小于平均值的进行提取
chars3 = ''.join([s for s in result if occ[s] < avg]) 
print(chars3)

#对 中间一个小写字母左右各三个大写字母的字符串 进行提取
chars4 = ''.join(re.findall(char_regex2, result2))
print(chars4)






