from marshmallow import fields, Schema

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String(255))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    surname = fields.Str()
    name = fields.Str()
    favorite_genre = fields.Str()
