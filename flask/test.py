from flask.globals import g


def func_a():
    return f'函数A，返回值{g.get("uname")}'
