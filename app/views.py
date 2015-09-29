import json
import time

from app import app, db
from app.models import Bill, Images
from flask import render_template, request, url_for, send_from_directory, Response, send_file
from flask.json import jsonify
import os
from werkzeug.utils import secure_filename, redirect


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

@app.route('/api/upload_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        new_name = str(int(time.time()))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
        user_id = request.form['user_id']
        db_entry = Images(new_name, os.path.splitext(filename)[1], user_id, time.time())
        db.session.add(db_entry)
        db.session.commit()
        return "true"

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file></p>
        <input type=hidden value='1' name='user_id'>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<id>')
def uploaded_file(id):
    db_object = Images.query.filter(Images.id == int(id)).first().image_name
    return send_file("../" + app.config['UPLOAD_FOLDER'] + db_object, mimetype='image/jpg')
