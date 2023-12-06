from flask import Flask
from bluep.views import user_bp
app = Flask(__file__)
app.register_blueprint(user_bp)
if __name__ == '__main__':
    app.run(debug=True)
