import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql:///myhealth')
UPLOAD_FOLDER = 'uploads/'
