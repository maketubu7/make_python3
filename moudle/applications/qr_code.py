from MyQR import myqr
from PIL import Image
import os

def show(image):
    im = Image.open(image)
    im.show()

def static_qr_code_builder(root_image):
    ''' 静态图片二维码 '''
    refile, ext = os.path.splitext(root_image)
    myqr.run(words='https://fanyi.youdao.com/',picture=root_image,colorized=True)
    show(refile+'_'+'qrcode.png')

def dynamic_qr_code_builder(root_gif):
    ''' 动态图片二维码 '''
    refile, ext = os.path.splitext(root_gif)
    myqr.run(words='https://www.baidu.com',picture=root_gif,colorized=True)
    show(refile+'_'+'qrcode.gif')

if __name__ == '__main__':
    static_qr_code_builder('love.jpg')
    # dynamic_qr_code_builder('wm.gif')