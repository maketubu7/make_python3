# -*- coding=utf-8 -*-

from PIL import Image
import argparse
import glob, os

#命令行输入参数处理  
parser = argparse.ArgumentParser()

#程序的参数定义 parser.add_argument() help=为--help的输出描述信息 type=为参数的类型
parser.add_argument('file', help='file')     #输入文件
parser.add_argument('-o', '--output',help='output file')   #输出文件
parser.add_argument('--width', help='output text width',type = int, default = 80) #输出字符画宽
parser.add_argument('--height', help='output text height',type = int, default = 80) #输出字符画高

#获取参数 parser.parse_args()
args = parser.parse_args()

# 定义相关参数
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值为256 但是字符集为70 通过切分 均分到70个字符集上
    unit = (256.0 + 1)/length
    # 按位置分配为每个像素对应的字符
    return ascii_char[int(gray/unit)]
def image_test():
    im = Image.open(IMG)
    im.rotate(90).show()

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    # txt = ""
    #获取每个点的像素值 写入到text文本中 每一行结束就换行
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件 不存在则在 主目录下创建一个文件输出
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
    
    # image_test()