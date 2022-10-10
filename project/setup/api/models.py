from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарантино'),
})

movie: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=250, example='США после Гражданской войны.'),
    'trailer': fields.String(required=True, max_length=100, example="https://www.youtube.com/watch?v=jfKfPfyJRdk"),
    'year': fields.Integer(required=True, example=2015),
    'rating': fields.Float(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='abc@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='123432'),
    'name': fields.String(required=True, max_length=100, example='Andrey'),
    'surname': fields.String(required=True, max_length=100, example='Popov'),
    'genre': fields.Nested(genre),
})
