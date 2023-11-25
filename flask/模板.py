from flask import Flask,render_template
from filters.index import MyFilter
from datetime import datetime

# 修改模板文件夹
app = Flask(__name__,template_folder='my')

MyFilter(app)

@app.route('/index/')
def index():
  my_dic = {
    'name':'yjw',
    'age':18,
    'param':10.5,
    'nickName':'',
    'turn':'<script>alert("hello")</script>',
    's':'444你好444',
    'ju':2,
    'nick':'吕布',
    'm':[1,2,3,4,5,6,7,8,9],
    'old_time':datetime(2023,11,25,15,50,0),
    'list':(1,2,3,5,8,9)
  }
  return render_template('test.html',**my_dic)

@app.route('/indexs/<int:id>')
def indexs(id):
  return 'succeed'


if __name__=='__main__':
  app.run(debug=True)
