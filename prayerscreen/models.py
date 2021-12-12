from prayerscreen import db
from datetime import datetime
import json


class Media(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    pic_src_1 = db.Column(db.String, nullable=True)
    pic_src_2 = db.Column(db.String, nullable=True)
    google_slide_src = db.Column(db.String, nullable=True)
    video_src = db.Column(db.String, nullable=True)

    def __init__(self, id, pic_src_1, pic_src_2, google_slide_src, video_src):
        self.id = id
        self.pic_src_1 = pic_src_1
        self.pic_src_2 = pic_src_2
        self.google_slide_src = google_slide_src
        self.video_src = video_src

    def __repr__(self):
        return '<Media %r>' % self.id



class PrayerTimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.column(db.DateTime)     
    fajr = db.Column(db.String, nullable=False)
    sunrise = db.Column(db.String, nullable=False)
    dhuhr = db.Column(db.String, nullable=False)
    asr = db.Column(db.String, nullable=False)
    maghrib = db.Column(db.String, nullable=False)
    isha = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<PrayerTimes %r>' % self.id


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
        return '<Settings %r>' % self.id


translate_keys = "monday,tuesday,wednesday,thursday,friday,saturday,sunday,january,february,march,april,may,june,july,august,september,october,november,december,am,pm,fajr,sunrise,dhuhr,asr,maghrib,isha,iqamah,next,begins,payer,turn_off_phones"
translate_values = json.loads(open('prayerscreen/translate_values.json').read())
default_translate_values = translate_values["en"]

# Translate class
class Translate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String, nullable=False, default='en')
    key = db.Column(db.String, nullable=False, default= translate_keys)
    value = db.Column(db.String, nullable=False, default= default_translate_values)
    
    def __repr__(self):
        return '<Translate %r>' % self.id


def init_db():
    db.create_all()

    # Create a test user
    new_settings = Settings(
        timezone=2,
        location="",
        latitude=0.0,
        longitude=0.0,
        fajr_iqamah=30,
        dhuhr_iqamah=10,
        asr_iqamah=10,
        maghrib_iqamah=0,
        isha_iqamah=10,
        fajr_iqamah_before_sunrise=False,
        iqamah_on=False,
        fajr_offset="",
        sunrise_offset="",
        dhuhr_offset="",
        asr_offset="",
        maghrib_offset="",
        isha_offset="",
        fixed_prayer_times=json.dumps({}),
        qr_code_on=True,
        time_format="24",
        date_format="%d/%m/%Y",
        prayertime_format="%H:%M",
        current_selected="Picture",
        slide_delay=5
        )
    db.session.add(new_settings)
    db.session.commit()

    new_translate = Translate(
        language='en',
        key=translate_keys,
        value=default_translate_values
        )
    db.session.add(new_translate)
    db.session.commit()

    new_media = Media(
        pic_src_1='',
        pic_src_2='',
        google_slide_src='',
        video_src=''
        )
    db.session.add(new_media)
    db.session.commit()

    new_prayer_times = PrayerTimes(
        date=datetime.now(),
        fajr='',
        sunrise='',
        dhuhr='',
        asr='',
        maghrib='',
        isha=''
        )
    db.session.add(new_prayer_times)
    db.session.commit()
    

if __name__ == '__main__':
    init_db()