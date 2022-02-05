from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ca79946617c662a483d0a5f0f1a179af'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase_modeling_systems.db'

data_base = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# it is necessary app to routes work correctly.
from general_system import routes
