from copyreg import constructor
from PIL import Image,ImageDraw,ImageFont
import random,numpy as np,cv2

# res = Image.open('./验证码/1.jpg')

# 图片大小
# print(res.size)

# 图片通道
# print(res.mode)

# 图片详细信息
# print(res.info)

# 图片修改大小
# res1 = res.resize((640,300))
# res1.show('2.jpg')

#图片旋转
# res1 = res.rotate(15)
# res1.save()
# res1.show()

# 翻转
# res1 = res.transpose(Image.FLIP_TOP_BOTTOM)
# res1 = res.transpose(Image.FLIP_LEFT_RIGHT)
# res1.show()
# res1.save('./验证码/2.jpg')

#生成验证码
# def get_color():
#   return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# def get_code():
#   width, height,font_size,font_num = 300,100,50,4
#   bg_color = get_color() # 生成背景色
#   image = Image.new('RGB',(width,height),bg_color) # 新建画布
#   draw = ImageDraw.Draw(image,'RGB')
#   font = ImageFont.truetype('./验证码/AlimamaDaoLiTi.ttf',font_size)

#   verify = ''
#   for i in range(font_num):
#     x,y = random.randint(i*(width/font_num),(i+1)*(width/font_num)-font_size),random.randint(0,height-font_size)
#     char = str(random.choice([chr(random.randint(65,90)),random.randint(0,9)]))
#     verify+=char
#     c = get_color()
#     draw.text((x,y),char,c,font)
#   return verify,image

# res = res.convert('L')
img = cv2.imread('./yzm/4.png')
def test1():
  # 降噪
  gs_img = cv2.GaussianBlur(img,(5,5),0)
  # cv2.imwrite('./yzm/4-1.png',gs_img)
  return gs_img

def test2():
  gs_img = test1()
  #边缘处理
  canny = cv2.Canny(gs_img,200,400)
  # cv2.imwrite('./yzm/4-2.png',canny)
  return canny

def test3():
  canny = test2()
  contours,h = cv2.findContours(canny,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
  for i,contour in enumerate(contours):
    x,y,w,h=cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
  cv2.imwrite('./yzm/4-3.png',img)

test3()
