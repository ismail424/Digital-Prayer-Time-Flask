from flask import render_template, request, redirect, Blueprint
from flask.scaffold import F
from requests.api import get
from prayerscreen.utils import *
from prayerscreen.new_prayer_times import *
from prayerscreen.socket.socket_routes import refresh
from prayerscreen import db
from prayerscreen.config import Config
from prayerscreen.models import *
from time import sleep
import json
import os
import socket

UPLOAD_FILE_SRC = Config.UPLOAD_FOLDER
api = Blueprint('api', __name__)


@api.route( '/' )
def index():
    return {'message': 'Hello, World!'}

@api.route( '/error' )
def error_text_file():
    error_list = open("prayerscreen/error.txt","r").readlines()
    return render_template( 'error.html' , error_list = error_list)

@api.route( '/sync' )
def sync():
    sync_time()
    return redirect("/")

@api.route( '/update' )
def update_now():
    update()
    return redirect("/")

@api.route( '/setup-realtimeclock' )
def realtimeclock():
    return setup_realtimeclock()

@api.route( '/prayertime' )
def prayertimes():
    prayertimes = PrayerTimes.query.all()
    return render_template( 'prayer_tabel.html', prayertimes = prayertimes )

@api.route( '/import/prayertime' , methods=["GET","POST"])
def import_prayertime():
    if request.method == 'POST':
        try:
            current_file = request.files["csv"]
            if len(current_file.filename) != 0:
                path = os.path.join(UPLOAD_FILE_SRC, current_file.filename)
                current_file.save(path)
                error_list = Check_CSV_prayertimes( path )
                if len(error_list) == 0:
                    print(DeleteTable("prayertimes"))
                    print(CreateTable( "prayertimes" ))
                    CSV_prayertimes( str(path) )
                else:
                    return render_template( 'error_csv.html', error_list = error_list )
            return redirect("/prayertime")
        except:
            pass
    return redirect("/")



@api.route( '/prayerscreen' )
def prayer_times():
    return render_template( 'prayer_times.html' )

@api.route( '/api/get_prayertimes' )
def api_get_prayertimes():
    prayer_times = get_prayertime_api()
    return prayer_times

@api.route( '/api/get_images' )
def api_get_images():
    images = get_images()
    return json.dumps(images)

@api.route( '/api/get_ip' )
def get_ip():
    try:
        settings = Settings.query.filter_by(id=1).first()
        qrcode_check = settings.qr_code_on
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            hostname = s.getsockname()[0]
            s.close()
        except:
            hostname = socket.gethostname()
            
        ip = str(socket.gethostbyname(hostname))
        
        return {"ip": ip, "qrcode_on": qrcode_check}
    except:
        return {"ip": "127.0.0.1", "qrcode_on": "false"}

@api.route( '/api/get_translation' )
def api_get_translation():
    translation = get_translation_json()
    return translation

@api.route( '/settings' )
def settings():
    settings =  get_settings()
    print(settings['fajr_iqamah_before_sunrise'])
    return render_template( 'settings.html' , settings = settings )

@api.route( '/advanced' )
def advanced():
    return render_template( 'advanced.html'  )



@api.route( '/save/settings', methods=["GET","POST"] )
def save_settings():
    if request.method == "POST":
        settings = dict(request.form)
        settings_values = list(settings.values())
        save_new_settings( settings_values )
        refresh()
        return redirect("/settings")
    else:
        return redirect("/")
    
@api.route( '/media' )
def media():
    images = get_images()
    try:
        url1 = os.path.join(UPLOAD_FILE_SRC, images["url_1"])
        url2 = os.path.join(UPLOAD_FILE_SRC, images["url_2"])
    except:
        url1 = ""
        url2 = ""
    return render_template( 'images.html', images = images, url1 = url1, url2 = url2)

@api.route( '/save/images', methods=["GET","POST"] )
def save_images():
    if request.method == "POST":
        
        try:
            for file in request.files:
                current_file = request.files[file]
                if len(current_file.filename) != 0:
                    path = os.path.join(UPLOAD_FILE_SRC, current_file.filename)
                    current_file.save(path)
        except Exception as e:
            save_error(e)
        try:
            image1 = request.files["image1"].filename
        except:
            image1 = request.form["image1"]
        
        try:
            image2 = request.files["image2"].filename
        except:
            image2 = request.form["image2"]
        
        try:
            video = request.files["video"].filename
        except:
            video = request.form["video_url"]

        google_slide_url = request.form["google_slide_url"]
        current_select = request.form["slide"]
        slide_delay = request.form["slide_delay"]

        values = [image1, image2, video, google_slide_url, current_select, slide_delay]
        save_new_images( values )
        refresh()
        return redirect("/images")
    else:
        return redirect("/")
    

@api.route( '/delete/file/<int:id>' )
def delete_file(id):
    if id in [1,2,3]:
        try:
            all_files = ["pic_src_1", "pic_src_2", "video_src"]
            fileToRemove  = all_files[id-1]
            full_media = Media.query.first()
            file_path = getattr(full_media, fileToRemove)
            if len(file_path) != 0:
                os.remove(os.path.join(UPLOAD_FILE_SRC, file_path))         
                            
            setattr(full_media, fileToRemove, '')
            db.session.commit()
              
        except Exception as e:
            save_error(e)
            return "Error deleting file"

    refresh()
    return redirect("/images")


@api.route( '/translate' )
def translate():
    translate = get_translation()
    the_key_values = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
             "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next_text" , "footer_text" ]
    translate = dict(zip(the_key_values, translate))
    return render_template( 'translate.html' , translate= translate)

@api.route( '/save/translate', methods=["GET","POST"] )
def save_translate():
    if request.method == "POST":
        translate = dict(request.form)
        translate_values = list(translate.values())
        save_new_translate_values( translate_values )
        refresh()
        return redirect("/translate")
    else:
        return redirect("/")  
        
@api.route( '/get_vaktija_eu' )
def get_vaktija_eu():
    return get_all_data_vakitja_eu()

@api.route( '/refresh' )
def refresh_now():
    refresh()
    return redirect("/")

