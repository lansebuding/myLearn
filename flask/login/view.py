from flask import render_template, Blueprint, request, make_response, session
import random
from datetime import datetime, timedelta
from components.codes import codes
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

@user_blue_print.route('/img/')
def get_image():
    image = codes().main()[1]
    response = make_response(image)
    response.content_type='image/png'
    return response

@user_blue_print.route('/set_cookie/')
def set_cookie():
    uname_cookie = request.cookies.get('Y-xxxx')
    response = None
    if uname_cookie:
        response = make_response(f'你的cookie是：{uname_cookie}')
    else:
        response = make_response('你的cookie已经到期，正在设置新cookie')
        # max_age 设置cookie有效时间，单位：秒
        # expires 设置cookie有效时间，datetime类型，具体到期时间，格林尼治时间，自动加8
        # expires 和 max_age都有，以max_age为准
        # expires=datetime.datetime(2023, 11, 28, 21, 0, 0)
        t = datetime.now()+timedelta(days=1, hours=16)  # t========两天后
        response.set_cookie(
            'Y-xxxx', str(random.randint(1, 50)), httponly=True, expires=t)
    return response


@user_blue_print.route('/set_session/')
def set_session():
    # 持久化----默认增加31天
    session.permanent = True

    # 服务器关闭，session有效期是之前系统保存的有效期
    # 服务器重启，秘钥不变则不会过期
    session['my_session'] = 'ITIT'
    return '设置了一个session对象'


@user_blue_print.route('/get_session/')
def get_session():
    return f'获取了一个session对象：{session.get("my_session")}'


@user_blue_print.route('/del_session/')
def del_session():
    session.pop('my_session')
    return f'删除了一个session对象：{session.get("my_session")}'
