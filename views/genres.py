from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from decorators import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_js = request.json
        genre_service.create(req_js)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):

    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        req_js = request.json
        req_js["id"] = gid
        genre_service.update(gid)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
