from flask import request
from flask_restx import Namespace, Resource

from implemented import author_service

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        req_js = request.json
        username = req_js.get("username", None)
        password = req_js.get("password", None)

        if None in [username, password]:
            return "", 400
        tokens = author_service.generate_token(req_js.get("username", None), req_js.get("password", None))

        return tokens, 201

    def put(self):
        req_js = request.json
        token = req_js.json("refresh_token")

        tokens = author_service.approve_refresh_token(token)

        return tokens, 201
