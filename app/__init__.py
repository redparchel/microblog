from flask import Flask
from flask.ext.sqlalchemy import SQLAlachemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlachemy(app)

from app import views, models
