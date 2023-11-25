from flask import Flask,request,url_for,redirect,Response,make_response
import random

app = Flask(__name__)

app.json.ensure_ascii=False

@app.route('/api/json')
def get_Indexs():
  # 可以直接返回字典，解决编码问题
  # return {
  #   'name':'你好'
  # }

  # 设置状态码
  # return '你好',200

  # 设置请求头
  # return '你好',{'Authortion':random.randint(100,200)}

  # 设置三个参数
  # return '你好',202,{'Authortion':random.randint(100,200)}

  # 列表形式-----响应内容，状态，header
  return '你好',202,[('Authortion',random.randint(1000,2000)),('Authortion-Two',random.randint(1000,2000))]

@app.route('/api/resp')
def ins():
  # return Response(response='你好',status=500,headers=[('AAA',100),('BBB',300)])
  res = make_response()
  res.response='你好吗'
  res.headers.add_header('ASAA','2222')
  res.status=202
  return res

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