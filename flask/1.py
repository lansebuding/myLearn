from flask import Flask,make_response,Response,render_template,session
# from flask_cors import CORS
# from io import BytesIO
import json

app = Flask(__name__)

# 解决跨域
# CORS(app)


@app.route('/main')
# 视图函数
def test():
  img = None
  with open('./yzm/1.jpg','rb') as f:
    img = f.read()
  response = make_response(img)
  response.content_type='image/jpg'
  return response

@app.route('/gis')
def gis():
  return render_template('1.html')

@app.route('/api/test')
def test_api():
  content={
    'resp_code':0,
    'resp_msg':'success',
    'data':['100','200']
  }
  return render_template('2.html',**content)

@app.route('/api/my-json',methods=['post', 'get'])
def test_my_json():
  dic = {
    'resp_code':0,
    'resp_msg':'success',
    'datas':{
      'name':'YJW',
      'age':25
    }
  }
  if isinstance(dic,dict):
    return json.dumps(dic)

@app.route('/set_session/')
def set_session():
  session['HHH']='123456'



if __name__ == '__main__':
  app.run(debug=True)