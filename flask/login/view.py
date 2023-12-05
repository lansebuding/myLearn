from flask import render_template, Blueprint, request, make_response, session, url_for, redirect, current_app, signals, send_from_directory
from flask.views import MethodView
from flask_wtf.file import FileRequired, FileAllowed
from flask.globals import g
import random
from datetime import datetime, timedelta
from components.codes import codes
from test import func_a
from blinker import Namespace
from wtforms import Form, StringField, FileField
from wtforms.validators import Length, ValidationError
from werkzeug.utils import secure_filename
import os

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'static')

user_blue_print = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static')

# 如果想要蓝图内地址，需要使用user.

s = Namespace()
s1 = s.signal('登录')


def login_log(*args, **kwargs):
    with open('log.log', 'a', encoding='utf8') as f:
        f.write(g.get('ip')+'\t已登录'+'\n')


s1.connect(login_log)


def render_template_func(*args, **kwargs):
    print('---------template_rendered')
    print(args)
    print(kwargs)
    print('---------template_rendered')


def render_template_func_before(*args, **kwargs):
    print('render_template_func_before---------')
    print(args)
    print(kwargs)
    print('render_template_func_before---------')


def render_template_func_error(*args, **kwargs):
    if kwargs.get('exception'):
        with open('log.log', 'a', encoding='utf8') as f:
            f.write(str(kwargs['exception'])+'\tin\t'+str(args[0])+'\n')


# flask内置信号template_rendered，before_render_template
# signals.template_rendered.connect(render_template_func)
# signals.before_render_template.connect(render_template_func_before)
# signals.got_request_exception.connect(render_template_func_error)


# 自定义校验
class LoginRigerter(Form):
    uname = StringField(validators=[Length(min=3, max=6, message='长度不对')])
    code = StringField(validators=[Length(min=4, max=4)])
    # pic = FileField(validators=[FileAllowed(['gif'],message='文件类型不允许'),FileRequired(message='文件未上传')])

    def validate_code(self, field: StringField):
        code = field.data
        _code = session.get('code')
        if _code != code:
            raise ValidationError(message='请输入正确的验证码')


@user_blue_print.route('/login/', methods=['get', 'post'])
def login():
    # v = 100/0
    # g.ip = request.remote_addr
    # s1.send()
    if request.method == 'get':
        return render_template('login.html')
    else:
        form = LoginRigerter(request.form)
        if form.validate():
            print('ok')
        else:
            print(form.errors)
        return render_template('login.html')


@user_blue_print.route('/register/')
def register():
    return '注册模块'


@user_blue_print.route('/upload_file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        res = request.files.get('pic')
        # 文件名的安全转换
        filename = secure_filename(res.filename)
        res.save(os.path.join(UPLOAD_PATH, filename))
        return filename


@user_blue_print.route('/get_file/<filename>/')
def get_file(filename):
    return send_from_directory(UPLOAD_PATH, filename)


@user_blue_print.route('/img/')
def get_image():
    code, image = codes().main()
    session['code'] = code
    response = make_response(image)
    response.content_type = 'image/png'
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
    # session.permanent = True

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


class LoginView(MethodView):
    def __jump(self, msg=None):
        return render_template('login.html', msg=msg)

    def get(self):
        # print(url_for('user.class_view_login'))
        print(current_app)
        return self.__jump()

    def post(self):
        uname, pwd = request.form.get('uname'), request.form.get('pwd')
        # 自定义表单校验
        form = LoginRigerter(request.form)
        print(form.validate())
        if uname == 'zss' and pwd == '123456':
            session['uname'] = uname
            return redirect(url_for('user.main'))
        else:
            return self.__jump('error')


@user_blue_print.route('/main/')
def main():
    if not session.get('uname'):
        return redirect(url_for('user.class_view_login'))
    else:
        return render_template('user.html')


@user_blue_print.route('/test_global/')
def test_global():
    # 设置全局变量，相互隔离
    g.uname = 'yjw'
    return func_a()

# 钩子函数，每次请求前执行


@user_blue_print.before_request
def before():
    print('hello')

# 钩子函数，返回值在模板中通用


@user_blue_print.context_processor
def before():
    # 此处定义的变量可以直接在模板使用
    return {'uname': '吕小布', 'server_error_500': '服务器出错啦', 'server_error_404': '页面没找到'}


@user_blue_print.route('/test_before_request/')
def test_before_request():
    # print(g.uname)
    return render_template('user.html')


single = Namespace()
my_single = single.signal('my_single')


def listen(*args, **kwargs):
    print('success')


my_single.connect(listen)


@user_blue_print.route('/test_single/<int:id>')
def test_single(id):
    my_single.send()
    return 'test_single'


"""
RESTful设计风格

1.数据传输使用json
2.url链接中只能有名词，不写动词
3.接口请求方式
    GET:从服务器获取资源
    POST:在服务器新增或者修改资源
    PUT:在服务器更新资源 (客户端提供所有改变后的数据)
    PATCH:在服务器更新资源 (客户端提供需要改变的属性)
    DELETE:从服务器删除资源
"""

user_blue_print.add_url_rule(
    '/class_view_login/', view_func=LoginView.as_view('class_view_login'))
