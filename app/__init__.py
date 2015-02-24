import os
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
from flask.ext.marshmallow import Marshmallow
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
db = SQLAlchemy(app)


from app import views, models
