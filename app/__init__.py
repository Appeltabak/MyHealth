from shutil import rmtree
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import User
from app import views

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True, convert_unicode=True)
# if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
#     print "Database not found, creating new..."
#     create_database(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

db.create_all()

try:  # Reset saved files on each start
    pass
    # rmtree(app.config['UPLOAD_FOLDER'], True)
    # os.mkdir(app.config['UPLOAD_FOLDER'])
except OSError:
    pass
