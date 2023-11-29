from PIL import Image,ImageFont,ImageDraw
import random
from io import BytesIO
# from flask import url_for


class codes:
    """
    生成验证码
    """
    def __init__(self) -> None:
        pass

    #生成验证码
    def get_color(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def get_code(self):
        width, height,font_size,font_num = 300,100,50,4
        bg_color = self.get_color() # 生成背景色
        image = Image.new('RGB',(width,height),bg_color) # 新建画布
        draw = ImageDraw.Draw(image,'RGB')
        # path = url_for('static',filename='fonts/AlimamaDaoLiTi.ttf')
        font = ImageFont.truetype(font='static/fonts/AlimamaDaoLiTi.ttf',size=font_size)

        verify = ''
        for i in range(font_num):
            x,y = random.randint(i*(width/font_num),(i+1)*(width/font_num)-font_size),random.randint(0,height-font_size)
            char = str(random.choice([chr(random.randint(65,90)),random.randint(0,9)]))
            verify+=char
            c = self.get_color()
            draw.text((x,y),char,c,font)
            by = BytesIO()
            image.save(by,'PNG')
        return verify,by.getvalue()

    def main(self):
        return self.get_code()
