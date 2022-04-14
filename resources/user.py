import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field is mandatory")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field is mandatory")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.findByUsername(data['username']) is not None:
            return {"message": "[INFO] An user with username {} already exists.".format(data['username'])}, 400

        user = UserModel(data['username'], data['password'])
        #user = UserModel(**data])
        user.saveToDB()

        return {"message": "[INFO] User with username {} is created successfully.".format(data['username'])}, 201
