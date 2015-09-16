from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

from app.models import User

engine = create_engine(os.environ.get('DATABASE_URL'), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

db.create_all()

admin = User('admin', 'test@test.com')
db.session.add(admin)
db.session.commit()
users = User.query.all()
print users
