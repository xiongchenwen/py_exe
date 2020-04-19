from PIL import Image

img1 = Image.open('tupian.jpg')
img1.show()
# 将每个像素都扩大2倍;eval()像素缩放处理
Image.eval(img1,lambda x:x*2).show()
# lambda匿名函数:冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。
# 其实lambda返回值是一个函数的地址，也就是函数对象。