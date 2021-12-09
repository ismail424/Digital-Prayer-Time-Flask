from datetime import datetime

from sqlalchemy.orm import defaultload
from sqlalchemy.sql.operators import nullslast_op
from prayerscreen import db

# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

# JSON for translate file
import json

class Media(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    pic_src_1 = db.Column(db.String, nullable=True)
    pic_src_2 = db.Column(db.String, nullable=True)
    google_slide_src = db.Column(db.String, nullable=True)
    video_src = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Media %r>' % self.name



class PrayerTimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.column(db.DateTime, nullable = False)        
    fajr = db.Column(db.String, nullable=False)
    sunrise = db.Column(db.String, nullable=False)
    dhuhr = db.Column(db.String, nullable=False)
    asr = db.Column(db.String, nullable=False)
    maghrib = db.Column(db.String, nullable=False)
    isha = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<PrayerTimes %r>' % self.name


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Time zone and location
    timezone = db.Column(db.Integer, default=2, nullable=True)
    location = db.Column(db.String, nullable=True)
    latitude = db.Column(db.Float, nullable=True, default=0.0)
    longitude = db.Column(db.Float, nullable=True, default=0.0)
    
    #Prayer iqamah
    fajr_iqamah = db.Column(db.Integer, default=30)
    dhuhr_iqamah = db.Column(db.Integer, default=10)
    asr_iqamah = db.Column(db.Integer, default=10)
    maghrib_iqamah = db.Column(db.Integer, default=0)
    isha_iqamah = db.Column(db.Integer, default=10)
    fajr_iqamah_before_sunrise = db.Column(db.Boolean, default=False)
    iqamah_on = db.Column(db.Boolean, default=False)
    
    #Prayer offsets
    fajr_offset = db.Column(db.String, nullable=True)
    sunrise_offset = db.Column(db.String, nullable=True)
    dhuhr_offset = db.Column(db.String, nullable=True)
    asr_offset = db.Column(db.String, nullable=True)
    maghrib_offset = db.Column(db.String, nullable=True)
    isha_offset = db.Column(db.String, nullable=True)
    
    # Fixed prayer times
    # JSON Object in string format
    fixed_prayer_times = db.Column(db.String, nullable=True, default='{}')
    
    #Extra settings
    qr_code_on = db.Column(db.Boolean, default=True)
    time_format = db.Column(db.String, nullable=True, default='24')
    date_format = db.Column(db.String, nullable=True, default='%d/%m/%Y')
    prayertime_format = db.Column(db.String(10), nullable=True)
    
    # Media settings
    current_selected = db.Column(db.String, nullable=False, default='Picture')
    slide_delay = db.Column(db.Integer, default=5, nullable=False)
    
    def __repr__(self):
        return '<Settings %r>' % self.name


translate_keys = "monday,tuesday,wednesday,thursday,friday,saturday,sunday,january,february,march,april,may,june,july,august,september,october,november,december,am,pm,fajr,sunrise,dhuhr,asr,maghrib,isha,iqamah,next,begins,payer,turn_off_phones"

# Translate class
class Translate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String, nullable=False, default='en')
    key = db.Column(db.String, nullable=False, default= translate_keys)
    value = db.Column(db.String, nullable=False, default= "translate_values_en")
    
    def __repr__(self):
        return '<Translate %r>' % self.name

if __name__ == '__main__':
    print("PrayerScreen models")
    # translate_values = json.dumps("prayerscreen/translate_values.json")
    # print(translate_values)
    #db.create_all()