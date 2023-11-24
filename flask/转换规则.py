import typing as t
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)


#自定义转换器规则
class PhoneCoverter(BaseConverter):
    regex = "1[3-9]\d{9}"

class liCoverter(BaseConverter):
    def to_python(self, value: str):
        return value.split('-')

#注册
app.url_map.converters['phone']=PhoneCoverter
app.url_map.converters['li']=liCoverter

@app.route('/api/phone/<phone:user_phone>')
def index(user_phone):
    return f'手机号是：{user_phone}'

@app.route('/api/phone_info/<li:info>')
def info(info):
    return f'手机号是：{info}'

if __name__=='__main__':
    app.run(debug=True)