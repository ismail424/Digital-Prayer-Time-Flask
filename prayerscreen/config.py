import os

class Config:
    SECRET_KEY = 'Secret key'
    UPLOAD_FOLDER = './static/upload'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prayerscreen/database.db'
