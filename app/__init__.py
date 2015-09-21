from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import User
from app import views

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
if not database_exists(engine.url):
        print "Database not found, creating new..."
        create_database(engine.url)

db.create_all()
