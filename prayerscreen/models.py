from datetime import datetime
from prayerscreen import db

# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


t_media = db.Table(
    'media',
    db.Column('url_1', db.Text),
    db.Column('url_2', db.Text),
    db.Column('google_slide_url', db.Text),
    db.Column('video_url', db.Text),
    db.Column('current_select', db.Text),
    db.Column('slide_delay', db.Text)
)



t_prayertimes = db.Table(
    'prayertimes',
    db.Column('date', db.Text),
    db.Column('fajr', db.Text),
    db.Column('sunrise', db.Text),
    db.Column('dhuhr', db.Text),
    db.Column('asr', db.Text),
    db.Column('maghrib', db.Text),
    db.Column('isha', db.Text)
)



t_settings = db.Table(
    'settings',
    db.Column('fajr_iqamah', db.Text),
    db.Column('dhuhr_iqamah', db.Text),
    db.Column('asr_iqamah', db.Text),
    db.Column('maghrib_iqamah', db.Text),
    db.Column('isha_iqamah', db.Text),
    db.Column('iqamah_on', db.Text),
    db.Column('id', db.Integer),
    db.Column('qrcode', db.NullType),
    db.Column('isha_fixed', db.Text),
    db.Column('fajr_iqamah_before_sunrise', db.Text)
)



t_translate = db.Table(
    'translate',
    db.Column('monday', db.Text),
    db.Column('tuesday', db.Text),
    db.Column('wednesday', db.Text),
    db.Column('thursday', db.Text),
    db.Column('friday', db.Text),
    db.Column('saturday', db.Text),
    db.Column('sunday', db.Text),
    db.Column('prayer', db.Text),
    db.Column('begins', db.Text),
    db.Column('iqamah', db.Text),
    db.Column('fajr', db.Text),
    db.Column('sunrise', db.Text),
    db.Column('dhuhr', db.Text),
    db.Column('asr', db.Text),
    db.Column('maghrib', db.Text),
    db.Column('isha', db.Text),
    db.Column('next_text', db.Text),
    db.Column('footer_text', db.Text)
)
