import json

from app import app
from app.models import Bill
from flask import render_template
from flask.json import jsonify


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/bills')
def display_bills():
    return render_template("index.html")


@app.route('/api/bills')
def bills():
    bills_collection = Bill.query.all()
    return json.dumps([x.json_data() for x in bills_collection])
