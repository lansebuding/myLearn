from PIL import Image,ImageDraw,ImageFont
import random

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
def get_color():
  return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

width, height,font_size,font_num = 300,100,50,4
bg_color = get_color() # 生成背景色
image = Image.new('RGB',(width,height),bg_color) # 新建画布
draw = ImageDraw.Draw(image,'RGB')
font = ImageFont.truetype('./验证码/AlimamaDaoLiTi.ttf',font_size)

verify = ''
for i in range(font_num):
  x,y = random.randint(i*(width/font_num),(i+1)*(width/font_num)-font_size),random.randint(0,height-font_size)
  char = str(random.choice([chr(random.randint(65,90)),random.randint(0,9)]))
  verify+=char
  c = get_color()
  draw.text((x,y),char,c,font)
# 65-122
print(verify)
print(chr(90))
image.show()