import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:7007@localhost/registration'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev_key'