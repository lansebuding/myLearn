"""
flask搭建api

docker部署
"""

from flask import Flask,make_response
from io import BytesIO
import random
from PIL import Image,ImageDraw,ImageFont

app = Flask(__name__)

#生成验证码
def get_color():
  return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def get_code():
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
  by = BytesIO()
  image.save(by,'PNG')
  return verify,by.getvalue()

@app.route('/img')

def main():
  verify,image = get_code()
  resp = make_response(image)
  resp.content_type='image/png'
  return resp

if __name__ == '__main__':
    app.run()
