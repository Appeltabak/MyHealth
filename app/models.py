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
