from flask import Flask
from item.view import product_blue_print
from login.view import user_blue_print
app = Flask(__name__)


# 注册蓝图
# url_prefix----加个前缀，区分
app.register_blueprint(user_blue_print, url_prefix='/user')
app.register_blueprint(product_blue_print, url_prefix='/product')

if __name__ == "__main__":
    app.run(debug=True)
