from flask import Flask, Blueprint
product_blue_print = Blueprint('items', __name__)


@product_blue_print.route('/item/')
def login():
    return '产品模块'
