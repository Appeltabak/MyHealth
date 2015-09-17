from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import User
from app import views

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)
session = Session()

db.create_all()
