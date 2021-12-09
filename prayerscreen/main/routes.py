from flask import Flask, render_template, request, redirect, Blueprint
from requests.api import get
from prayerscreen.help_functions import *
from prayerscreen.new_prayer_times import *
from prayerscreen.socket.socket_routes import refresh
from prayerscreen import db
from time import sleep
import sqlite3
import json
import os
import socket


main = Blueprint('main', __name__)

@main.route( '/' )
def home():
    # Get the current prayer times from the database
    prayer_times = db.session.query('prayer_times').all()
    print(prayer_times)
    return render_template( 'index.html' )

@main.route( '/error' )
def error():
    print("nice")
    error_list = open("error.txt","r").readlines()
    return render_template( 'error.html' , error_list = error_list)


@main.route( '/sync' )
def sync():
    sync_time()
    return redirect("/")

@main.route( '/update' )
def update_now():
    update()
    return redirect("/")

@main.route( '/setup-realtimeclock' )
def realtimeclock():
    x = setup_realtimeclock()
    return x

@main.route( '/prayertime' )
def prayertimes():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""select * from prayertimes""")
    prayertimes = c.fetchall()     
    return render_template( 'time.html', prayertimes = prayertimes )

@main.route( '/import/prayertime' , methods=["GET","POST"])
def import_prayertime():
    if request.method == 'POST':
        try:
            current_file = request.files["csv"]
            if len(current_file.filename) != 0:
                path = os.path.join(app.config['UPLOAD_FOLDER'], current_file.filename)
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



@main.route( '/prayerscreen' )
def prayer_times():
    return render_template( 'prayer_times.html' )

@main.route( '/api/get_prayertimes' )
def api_get_prayertimes():
    prayer_times = get_prayertime_api()
    return prayer_times

@main.route( '/api/get_images' )
def api_get_images():
    images = get_images()
    return json.dumps(images)

@main.route( '/api/get_ip' )
def get_ip():
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""select qrcode from settings """)
        qrcode_check = c.fetchone()
        qrcode_check = qrcode_check[0]
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            hostname = s.getsockname()[0]
            s.close()
        except:
            hostname = socket.gethostname()
        ip = str(socket.gethostbyname(hostname))
        ip_json = '{"ip":"'+ip+'", "qrcode_on":"'+str(qrcode_check.lower())+'"}'
        return json.loads(ip_json)
    except:
            ip_json = '{"ip":"0", "qrcode_on":"true"}}'
            return json.loads(ip_json)

@main.route( '/api/get_translation' )
def api_get_translation():
    translation = get_translation_json()
    return translation

@main.route( '/settings' )
def settings():
    settings =  get_settings()
    print(settings['fajr_iqamah_before_sunrise'])
    return render_template( 'settings.html' , settings = settings )

@main.route( '/advanced' )
def advanced():
    return render_template( 'advanced.html'  )



@main.route( '/save/settings', methods=["GET","POST"] )
def save_settings():
    if request.method == "POST":
        settings = dict(request.form)
        settings_values = list(settings.values())
        save_new_settings( settings_values )
        refresh()
        return redirect("/settings")
    else:
        return redirect("/")
    
@main.route( '/images' )
def images():
    images = get_images()
    try:
        url1 = os.path.join(app.config['UPLOAD_FOLDER'], images["url_1"])
        url2 = os.path.join(app.config['UPLOAD_FOLDER'], images["url_2"])
    except:
        url1 = ""
        url2 = ""
    return render_template( 'images.html', images = images, url1 = url1, url2 = url2)

@main.route( '/save/images', methods=["GET","POST"] )
def save_images():
    if request.method == "POST":
        
        try:
            for file in request.files:
                current_file = request.files[file]
                if len(current_file.filename) != 0:
                    path = os.path.join(app.config['UPLOAD_FOLDER'], current_file.filename)
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
    

@main.route( '/delete/file/<id>' )
def delete_file(id):
    if id == "1" or id == "2" or id == "3":
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        file_list = ["url_1", "url_2", "video_url"]
        remove_current_file  = file_list[int(id)-1]
        try:
            c.execute("SELECT {} from images".format(remove_current_file))
            file_path = c.fetchone()[0]
            if len(file_path) != 0:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_path))            
        except Exception as e:
            save_error(e)
        try:
            c.execute("""UPDATE images SET {} = '' """.format(remove_current_file))
            conn.commit()  
            
        except Exception as e:
            save_error(e)
    refresh()
    return redirect("/images")



@main.route( '/translate' )
def translate():
    translate = get_translation()
    the_key_values = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
             "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next_text" , "footer_text" ]
    translate = dict(zip(the_key_values, translate))
    return render_template( 'translate.html' , translate= translate)

@main.route( '/save/translate', methods=["GET","POST"] )
def save_translate():
    if request.method == "POST":
        translate = dict(request.form)
        translate_values = list(translate.values())
        save_new_translate_values( translate_values )
        refresh()
        return redirect("/translate")
    else:
        return redirect("/")    
        
@main.route( '/get_vaktija_eu' )
def get_vaktija_eu():
    return get_all_data_vakitja_eu()

@main.route( '/refresh' )
def refresh_now():
    refresh()
    return redirect("/")
