#Import Flask and SOCKET.IO
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

#Import SQL
import sqlite3

#import help-functions from another python file
from help_functions import *

#import JSON
import json

app = Flask(__name__)

#This secret key dosen't do anything but you need this!
app.config[ 'SECRET_KEY' ] = 'Secret key'
socketio = SocketIO( app )

@app.route( '/' )
def home():
    return render_template( 'index.html' )

@app.route( '/prayerscreen' )
def prayer_times():
    return render_template( 'prayer_times.html' )


@app.route( '/api/get_prayertimes' )
def api_get_prayertimes():
    prayer_times = get_prayertime_api()
    return prayer_times

@app.route( '/api/get_ip' )
def get_ip():
    ip = str(request.remote_addr)
    ip_json = '{"ip":"'+ip+'"}'
    return json.loads(ip_json)

@app.route( '/api/get_translation' )
def api_get_translation():
    translation = get_translation_json()
    return translation

@app.route( '/settings' )
def settings():
    return render_template( 'settings.html' )

@app.route( '/images' )
def images():
    return render_template( 'images.html' )

@app.route( '/translate' )
def translate():
    translate = get_translation()
    the_key_values = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
             "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next_text" , "footer_text" ]
    translate = dict(zip(the_key_values, translate))
    return render_template( 'translate.html' , translate= translate)

@app.route( '/save/translate', methods=["GET","POST"] )
def save_translate():
    if request.method == "POST":
        translate = dict(request.form)
        translate_values = list(translate.values())
        save_new_translate_values( translate_values )
        refresh()
        return redirect("/translate")
    else:
        return redirect("/")

@app.route( '/refresh' )
def refresh_now():
    refresh()
    return redirect("/")

    
@socketio.on( 'my event' )
def event( data ):
    print(data) 

def refresh():
    socketio.emit("refresh")

if __name__ == '__main__':

    #Debug only
    # socketio.run( app, debug = True, port = 80 )

    #Server (LAN)
    socketio.run(app, host='0.0.0.0',debug = True, port=80)

