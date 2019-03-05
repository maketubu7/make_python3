import zipfile, re, chardet

findnothing = re.compile(r"Next nothing is (\d+)").match
comments = []  # 收集注释信息的列表
z = zipfile.ZipFile("channel.zip", "r")  # 读取压缩包文件
seed = "90052"

while True:
    fname = seed + ".txt"
    comments.append((z.getinfo(fname).comment).decode()) # 要把bytes转化为str，否则最后的print会报错
    guts = (z.read(fname)).decode() # 要把bytes转化为str，否则findnothing会报错
    m = findnothing(guts)
    if m:
        seed = m.group(1)
    else:
        break
def test():
    text = 'Next nothing is 94191'
    m = findnothing(text)
    print(m.group(1))

print("".join(comments))  # 打印所有注释信息
test()

