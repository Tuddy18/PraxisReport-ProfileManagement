from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_selfdoc import Autodoc


app = Flask(__name__)
auto = Autodoc(app)

CORS(app, resources={r"/*": {"origins": "*"}})
db_url = 'mysql://' + config['MYSQL_USER'] + ':' + config['MYSQL_PASSWORD'] + '@' + config['MYSQL_HOST'] + '/' + config['MYSQL_DB']
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

from app.domain import *
from app.service import profile_service

# db.drop_all()
db.create_all()

jwt = JWTManager(app)

