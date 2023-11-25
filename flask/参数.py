from flask import Flask

app = Flask(__name__)

@app.route('/api/detail/<int:id>')
def index(id):
  print(id)
  return f"id={id}"

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)