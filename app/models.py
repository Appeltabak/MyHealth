from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email
        )


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    price = db.Column(db.Numeric)
    id_medical_entity = db.Column(db.Integer)
    id_user = db.Column(db.Integer)

    def __init__(self, description, price, id_medical_entity, id_user):
        self.description = description
        self.price = price
        self.id_medical_entity = id_medical_entity
        self.id_user = id_user

    def to_dict(self):
        return dict(
            id=self.id,
            description=self.description,
            price=str(self.price),
            id_medical_entity=self.id_medical_entity,
            id_user=self.id_user
        )

class ECGdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_timestamp = db.Column(db.Integer)
    offset = db.Column(db.Integer)
    value = db.Column(db.Numeric)

    def __init__(self, start_timestamp, offset, value):
        self.start_timestamp = start_timestamp
        self.offset = offset
        self.value = value

class BloodPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer)
    overdruk = db.Column(db.Integer)
    onderdruk = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
    def __init__(self, timestamp, overdruk, onderdruk, user_id):
        self.timestamp = timestamp
        self.overdruk = overdruk
        self.onderdruk = onderdruk
        self.user_id = user_id

class Pulse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
    def __init__(self, timestamp, value, user_id):
        self.timestamp = timestamp
        self.value = value
        self.user_id = user_id

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String)
    extension = db.Column(db.String)
    user_id = db.Column(db.Integer)
    upload_time = db.Column(db.Integer)

    def __init__(self, image_name, extension, user_id, upload_time):
        self.image_name = image_name
        self.user_id = user_id
        self.upload_time = upload_time
        self.extension = extension
