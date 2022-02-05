from general_system import data_base
from datetime import datetime


class User(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    username = data_base.Column(data_base.String, nullable=False)
    email = data_base.Column(data_base.String, nullable=False, unique=True)
    password = data_base.Column(data_base.String, nullable=False)
    perf_photo = data_base.Column(data_base.String, default='default.jpg')
    posts = data_base.relationship('Post', backref='autor', lazy=True)
    courses = data_base.Column(data_base.String, nullable=False, default='Não Informado')


class Post(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    title = data_base.Column(data_base.String, nullable=False)
    bory_text = data_base.Column(data_base.Text, nullable=False)
    date_creation = data_base.Column(data_base.DateTime, default=datetime.utcnow, nullable=False)
    id.user = data_base.Column(data_base.Integer, data_base.ForeignKey('user.id'), nullable=False)