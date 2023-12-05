from flask import Flask, current_app, render_template, signals
from item.view import product_blue_print
from login.view import user_blue_print
from os import urandom
from blinker import Namespace
from datetime import timedelta
app = Flask(__name__)


class BaseConfig:
    DEBUG = True
    # SECRET_KEY = 'YJW123456'
    SECRET_KEY = urandom(24)
    # 设置session持久化时间
    # PERMANENT_SESSION_LIFETIME = timedelta(days=1)


app.config.from_object(BaseConfig)
# 注册蓝图
# url_prefix----加个前缀，区分
app.register_blueprint(user_blue_print, url_prefix='/user')
app.register_blueprint(product_blue_print, url_prefix='/product')

# 创建上下文
ctx = app.app_context()
ctx.push()
# print(current_app)


@app.errorhandler(404)  # 这是未定义路径的错误处理 ，在有路径的错误需加入try-except处理
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_(error):
    return render_template('500.html'), 500


# 信号
# 定义信号
# space = Namespace()
# fire_space = space.signal('FIRE!')
# 监听信号


# @signals.request_started.connect
# def lisen(*args, **kwargs):
#     print('app信号监听成功')


# fire_space.connect(lisen)

# 发送信号
# fire_space.send()

@app.route('/signal/')
def signal_send():
    return 'yes'


if __name__ == "__main__":
    app.run()
