from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        result = user_service.get_all()
        return UserSchema(many=True).dump(result), 200

    def post(self):
        req_js = request.json
        user_service.create(req_js)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):

    def get(self, uid):
        result = user_service.get_one(uid)
        return UserSchema().dump(result), 200

    def put(self, uid):
        req_js = request.json
        if 'id' not in req_js:
            req_js["id"] = uid
        user_service.update(uid)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
