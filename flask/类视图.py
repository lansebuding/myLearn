from flask import Flask, render_template, url_for, request
from flask.views import View, MethodView
from functools import wraps
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder='my')


class BaseView(View):
    pass


class ListView(BaseView):
    """
    类视图
    """

    def dispatch_request(self):
        return '这是类视图'


def desc(func: 'function'):
    # @wraps(func)
    def inner(*args, **kargs):
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        if username == 'zs' and pwd == '123456':
            logging.info('登入成功')
        else:
            logging.info('登入失败')
        return func(*args, **kargs)
    return inner


class LoginView(MethodView):
    decorators = [desc]

    def __jump(self, msg=None):
        return render_template('login.html', msg=msg)

    def get(self, v='444444444'):
        return self.__jump()

    def post(self):
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        if username == 'zs' and pwd == '123456':
            return 'success'
        else:
            return self.__jump('用户名或者密码错误')


app.add_url_rule('/list/', view_func=ListView.as_view('myList'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))


# @app.route('/login/', methods=['post', 'get'])
# @desc
# def lg():
#     return render_template('login.html')

# 不必打开浏览器测试
# with app.test_request_context():
#     print(url_for('myList'))


if __name__ == '__main__':
    app.run(debug=True)
