from flask import request
from flask_restx import Namespace, Resource

from implemented import author_service, user_service

auth_ns = Namespace("auth")


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_js = request.json
        email = req_js.get("email", None)
        password = req_js.get("password", None)

        if None in [email, password]:
            return "", 400
        tokens = author_service.generate_token(req_js.get("email", None), req_js.get("password", None))

        return tokens, 201

    def put(self):
        req_js = request.json
        token = req_js.get("refresh_token")

        tokens = author_service.approve_refresh_token(token)

        return tokens, 201


@auth_ns.route("/register")
class AuthsView(Resource):
    def post(self):
        req_js = request.json
        user_service.create(req_js)
        return "", 201
