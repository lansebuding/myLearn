from flask import Flask,render_template,make_response,request
import crawler
import json
app = Flask(__name__)

@app.route('/')
def number():
  return render_template('1.html')

@app.route('/api/test')
def test():
  my_json = crawler.get_data(request.args.get('value'))
  return make_response(json.dumps({'resp_code':0,'resp_msg':'success','datas':my_json}))


if __name__ == '__main__':
  app.run(debug=True)