from prayerscreen import db
from sqlalchemy import Column, Float, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    selected = Column(Text, nullable=False)
    delay = Column(Integer, nullable=False)
    img = Column(Text, nullable=False)
    video = Column(Text, nullable=False)
    google_slide = Column(Text)
    text_titel = Column(Text)
    text_body = Column(Text)


class PrayerTime(Base):
    __tablename__ = 'PrayerTimes'

    id = Column(Integer, primary_key=True)
    date = Column(Text, nullable=False)
    fajr = Column(Text, nullable=False)
    sunrise = Column(Text, nullable=False)
    dhuhr = Column(Text, nullable=False)
    asr = Column(Text, nullable=False)
    maghrib = Column(Text, nullable=False)
    isha = Column(Text, nullable=False)


class PrayerTimesIqamah(Base):
    __tablename__ = 'PrayerTimesIqamah'

    id = Column(Integer, primary_key=True)
    fajr_iqamah = Column(Integer, nullable=False)
    dhuhr_iqamah = Column(Integer, nullable=False)
    asr_iqamah = Column(Integer, nullable=False)
    maghrib_iqamah = Column(Integer, nullable=False)
    isha_iqamah = Column(Integer, nullable=False)


class Setting(Base):
    __tablename__ = 'Settings'

    id = Column(Integer, primary_key=True)
    time_format = Column(Text)
    timezone = Column(Float(8, 2))
    city = Column(Text)
    country = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    iqamah_on = Column(Integer, nullable=False)
    prayer_offset = Column(Text)
    fixed_prayer_times = Column(Text)
    qr_code_on = Column(Integer, nullable=False)
    date_format = Column(Text)
    current_style_id = Column(Integer, nullable=False)


class Translate(Base):
    __tablename__ = 'Translate'

    id = Column(Integer, primary_key=True)
    current_language = Column(Text, nullable=False)
    monday = Column(Text, nullable=False)
    tuesday = Column(Text, nullable=False)
    wednesday = Column(Text, nullable=False)
    thursday = Column(Text, nullable=False)
    friday = Column(Text, nullable=False)
    saturday = Column(Text, nullable=False)
    sunday = Column(Text, nullable=False)
    january = Column(Text, nullable=False)
    february = Column(Text, nullable=False)
    march = Column(Text, nullable=False)
    april = Column(Text, nullable=False)
    may = Column(Text, nullable=False)
    june = Column(Text, nullable=False)
    july = Column(Text, nullable=False)
    august = Column(Text, nullable=False)
    september = Column(Text, nullable=False)
    october = Column(Text, nullable=False)
    november = Column(Text, nullable=False)
    december = Column(Text, nullable=False)
    AM = Column(Text, nullable=False)
    PM = Column(Text, nullable=False)
    fajr = Column(Text, nullable=False)
    sunrise = Column(Text, nullable=False)
    dhuhr = Column(Text, nullable=False)
    asr = Column(Text, nullable=False)
    maghrib = Column(Text, nullable=False)
    isha = Column(Text, nullable=False)
    iqamah = Column(Text, nullable=False)
    next = Column(Text, nullable=False)
    begins = Column(Text, nullable=False)
    prayer = Column(Text, nullable=False)
    mobile_phones = Column(Text, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)
