from PIL import Image,ImageFilter
import glob, os

def filter_blur(file):
    ''' 图片模糊滤镜处理 '''
    # BLUR	模糊    模糊光圈处理
    # CONTOUR	轮廓  类似素描画
    # DETAIL	详情
    # EDGE_ENHANCE	EDGE_ENHANCE
    # EDGE_ENHANCE_MORE	EDGE_ENHANCE_MORE
    # EMBOSS	EMBOSS
    # FIND_EDGES	寻找边缘  类似浮雕
    # SHARPEN	SHARPEN
    # SMOOTH	平滑
    # SMOOTH_MORE	SMOOTH_MORE
    refile, ext = os.path.splitext(file)
    im = Image.open(file)
    mode = ImageFilter.CONTOUR
    # 应用模糊滤镜:
    im2 = im.filter(mode)
    im2.show()
    # im2.save(refile+'-'+mode.name+'.jpg', 'jpeg')

def zoom(file):
    ''' 图片缩放 '''
    refile, ext = os.path.splitext(file)
    im = Image.open(file)
    #  获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到50%:
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' % (w//2, h//2))
    # 把缩放后的图像用jpeg格式保存:
    im.save(refile+'-zoom.jpg', 'jpeg')

if __name__ == '__main__':
    filter_blur('歌词分享_1466179342779.jpg')
    # zoom('歌词分享_1466179342779.jpg')