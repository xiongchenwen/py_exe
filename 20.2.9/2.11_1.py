from PIL import Image, ImageDraw

# 按尺寸缩放图片:thumbnail指定大小
img = Image.open('tupian.jpg')
w, h = img.size
draw_obj = ImageDraw.Draw(img)
draw_obj.line((0, 0, w, h), fill='red', width=2)
draw_obj.line((w, 0, 0, h), fill='red', width=2)
img.show()
