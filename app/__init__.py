from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import User
from app import views

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True,
                       convert_unicode=True)

db.create_all()
