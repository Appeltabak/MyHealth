import json
import time

from app import app
from app.models import Bill
from flask import render_template


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/bills')
def display_bills():
    return render_template("index.html")


@app.route('/api/bills')
def bills():
    bills_collection = Bill.query.all()
    return json.dumps([b.to_dict() for b in bills_collection])


@app.route('/api/user_verification/<username>/<password>')
def user_verification(username, password):
    if username == "jan" and password == 'password':
        return json.dumps({
            'id': 0
        })
    else:
        return 'Error', 401


@app.route('/api/measurements/<id>')
def get_measurements(id):
    return json.dumps({
        'id': 0,
        'value': 5,
        'date': time.time()
    })


@app.route('/api/userinfo/<id>')
def get_userinfo(id):
    #user = User.query.one()
    #return json.dumps(user.to_dict())
    return json.dumps({
        'id': 0,
        'username': "jan",
        'email': "jan@gmail.com"
    })
