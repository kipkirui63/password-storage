from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restx import Api, Namespace, Resource
from .models import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


CORS(app)


db.init_app(app)
migrate=Migrate(app,db)
ma =  Marshmallow(app)
server = Api(app)

from server import routes , models




