import os

class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
