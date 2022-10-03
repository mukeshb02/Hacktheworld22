from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object('config')
app.logger.setLevel(logging.DEBUG)

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.logger.info('app initialized')

from .models import users
from .routes import routes

# https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables
db.create_all()
db.session.commit()
