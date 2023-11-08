from PIL import Image,ImageDraw,ImageFont
import random

# image = Image.new('RGB',(500,200),(0,0,0))
# image.save('./验证码/底图.png')

def draws():
  img = Image.open('./验证码/底图.png')
  font = ImageFont.truetype('./验证码/AlimamaDaoLiTi.ttf',30)
  t = '哈哈哈'
  width,height = img.size
  w,h = font.getsize(t)
  draw = ImageDraw.Draw(img,'RGB')
  c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  draw.text(((width-w)/2,height/2-h/2),t,c,font)
  img.show()
  # img.save()

if __name__ == '__main__':
  draws()