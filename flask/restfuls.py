from flask import Flask, url_for
from flask_restful import Resource, Api, inputs
# 参数校验
from flask_restful.reqparse import RequestParser, Argument

app = Flask(__file__)
api = Api(app=app)
app.config.from_pyfile('setting.py')


class itemView(Resource):
    def get(self):
        return {'name': 'YJW', 'age': 100, 'url': url_for('item')}

    def post(self):
        # 解析器
        parser = RequestParser()
        # 添加解析规则
        parser.add_argument(name='uname', type=str, location="form",
                            trim=True, required=True, help="用户名验证错误")
        parser.add_argument(name='gender', location='form',
                            required=True, choices=['男', '女'], help="gender验证错误")
        parser.add_argument(name='phone', location='form',
                            required=True, type=inputs.regex('^1[356789]\d{9}$'), help="phone验证错误")
        parser.add_argument(name='date', location='form',
                            required=True, type=inputs.date, help="phone验证错误")
        # 解析数据
        args = parser.parse_args()
        print(args)
        return {'msg': 'success', 'code': 200}


# 注册
api.add_resource(itemView, '/item/', endpoint='item')

if __name__ == '__main__':
    app.run()
