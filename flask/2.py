from flask import Flask
import json

app = Flask(__name__)

class Config:
  DEBUG = True

@app.route('/')
def index():
  return '111'

if __name__ == '__main__':
  # print(app.config)
  # app.config.update({'DEBUG':True})
  # app.config.from_file('config.json',json.load)
  # app.config.from_pyfile('setting.py')
  app.config.from_object(Config)
  app.run(host='0.0.0.0')