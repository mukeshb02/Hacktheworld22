import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.sample(random_str, 16))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@localhost:3306/flask_rest_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key