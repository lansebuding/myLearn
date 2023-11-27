from flask import render_template, Blueprint
user_blue_print = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static')

# 如果想要蓝图内地址，需要使用user.


@user_blue_print.route('/login/')
def login():
    return render_template('user.html')


@user_blue_print.route('/register/')
def register():
    return '注册模块'


@user_blue_print.route('/logout/')
def logout():
    return '登出模块'
