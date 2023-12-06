from flask.blueprints import Blueprint
from flask_restful import Resource, Api


user_bp = Blueprint('my', __name__)
api = Api(user_bp)


class LoginView(Resource):
    def get(self):
        return {'msg': 'success'}


api.add_resource(LoginView, '/login/', endpoint='login')
