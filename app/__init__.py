from shutil import rmtree
import time
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import *
from app import views

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True, convert_unicode=True)
# if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
#     print "Database not found, creating new..."
#     create_database(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

db.create_all()

deleted = False


def reset_images():
    rmtree(app.config['UPLOAD_FOLDER'], True)
    os.mkdir(app.config['UPLOAD_FOLDER'])
    db.session.query(Images).delete()
    db.session.commit()


def remove_db():
    print User.query.delete()
    print Bill.query.delete()
    print ECGdata.query.delete()
    print BloodPressure.query.delete()
    print Pulse.query.delete()
    print Images.query.delete()
    db.session.commit()


def populate_ecg():
    timestamp = time.time()
    current_index = 0
    while current_index < 50:
        for x in range(0, 10):
            ecgdata = ECGdata(timestamp, current_index * 100, 0)
            db.session.add(ecgdata)
            current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0.2)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, -0.1)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 1)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, -0.2)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0.2)
        db.session.add(ecgdata)
        current_index += 1
        ecgdata = ECGdata(timestamp, current_index * 100, 0)
        db.session.add(ecgdata)
        current_index += 1
    db.session.commit()



def populate_db():
    admin = User("admin", "test@test.com")
    db.session.add(admin)

    bill = Bill("First test Bill", 10, 1, 1)
    db.session.add(bill)
    bill = Bill("Second test Bill", 11.5, 1, 1)
    db.session.add(bill)
    bill = Bill("Third test Bill", 15, 1, 1)
    db.session.add(bill)

    bp = BloodPressure(time.time(), 80, 120, 1)
    db.session.add(bp)
    bp = BloodPressure(time.time(), 81, 119, 1)
    db.session.add(bp)
    bp = BloodPressure(time.time(), 79, 121, 1)
    db.session.add(bp)

    pulse = Pulse(time.time(), 80, 1)
    db.session.add(pulse)
    pulse = Pulse(time.time(), 81, 1)
    db.session.add(pulse)
    pulse = Pulse(time.time(), 79, 1)
    db.session.add(pulse)
    pulse = Pulse(time.time(), 82, 1)
    db.session.add(pulse)

    populate_ecg()

    db.session.commit()


try:  # Reset saved files on each start
    if app.debug and deleted is False:
        print "populating db..."
        reset_images()
        remove_db()
        populate_db()
        print "done!"
        deleted = True
except OSError:
    pass
