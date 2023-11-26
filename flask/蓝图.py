from flask import Flask, Blueprint

app = Flask(__name__)

user_blue_print = Blueprint('user', __name__)


@user_blue_print.route('/login/')
def login():
    return '登录模块'


@user_blue_print.route('/register/')
def register():
    return '注册模块'


@user_blue_print.route('/logout/')
def logout():
    return '登出模块'


# 注册蓝图
# url_prefix----加个前缀，区分
app.register_blueprint(user_blue_print, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
