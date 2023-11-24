from flask import Flask,request,url_for

app = Flask(__name__)


@app.route('/api/test/<int:id>')
def get_Index(id):
  return f'id是：1111111--{id}'

@app.route('/api/test_param',methods=['GET'])
def get_Index2():
  username = request.args.get('username')
  pwd = request.args.get('pwd')
  return f'username={username},pwd={pwd}'

@app.route('/api/test_form',methods=['POST'])
def get_Index3():
  username = request.form.get('username')
  pwd = request.form.get('pwd')
  return f'username={username},pwd={pwd}'

@app.route('/api/front/upload',methods=['POST'])
def get_Index4():
  # pic是key
  f = request.files.get('pic')
  print(f.filename)
  try:
    with open(f'./flask/imgs/{f.filename}','wb') as file:
      file.write(f.read())
  except Exception as err:
    return '上传失败'
  return '上传成功'

@app.route('/api/args',methods=['POST','GET'])
def get_Index5():
  url = request.url
  method = request.method
  user = request.headers['User-Agent']
  uid = request.cookies.get('uuid')
  return f'succeed---{url}---{method}---{user}==={uid}'

# 反向查找 函数对应的路由
@app.route('/api/url_for',methods=['POST','GET'])
def get_Index6():
  url = url_for('get_Index',id=10)
  return f'succeed---{url}'

if __name__ == "__main__":
  app.run(debug=True)