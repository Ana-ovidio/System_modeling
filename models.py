from main import data_base
from datetime import datetime

class User (data_base.Model):
    id= data_base.column(data_base.Integer, primary_key=True)
    username= data_base.column(data_base.String, nullable=False)
    email= data_base.column(data_base.String, nullable=False, unique=True)
    password= data_base.column(data_base.String, nullable=False)
    perfil_photo= data_base.column(data_base.String, default='default.jpg')

class Post (data_base.Model):
    id= data_base.column(data_base.Integer, primary_key=True)
    title= data_base.column(data_base.String, nullable=False)
    bory_text= data_base.column(data_base.Text, nullable=False)
    date_creation= data_base.column(data_base.Datetime, nullable=False, default=datetime.utcnow)