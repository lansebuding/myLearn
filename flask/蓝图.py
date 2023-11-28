from flask import Flask
from item.view import product_blue_print
from login.view import user_blue_print
from os import urandom
from datetime import timedelta
app = Flask(__name__)


class BaseConfig:
    DEBUG = True
    # SECRET_KEY = 'YJW123456'
    SECRET_KEY = urandom(24)
    # 设置session持久化时间
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)


app.config.from_object(BaseConfig)
# 注册蓝图
# url_prefix----加个前缀，区分
app.register_blueprint(user_blue_print, url_prefix='/user')
app.register_blueprint(product_blue_print, url_prefix='/product')

if __name__ == "__main__":
    app.run()
