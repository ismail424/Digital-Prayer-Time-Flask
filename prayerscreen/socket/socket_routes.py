from types import FrameType


from prayerscreen import socketio
from prayerscreen.utils import *

@socketio.on('new-prayertime-salahtimes')
def new_prayertime_salahtimes(json):
    try:
        url = str(json["data"])
        original_url = url + "/render"
        url = url[27:].strip()
        list = url.split("/")
        country = list[0]
        city = list[1]
        print(original_url, country, city)
        if internet_on():
            try:
                if CheckURL(original_url):
                    print(DeleteTable("prayertimes"))
                    print(CreateTable( "prayertimes" ))
                    print(NewPrayerTime( original_url, country, city ))     
                    socketio.emit("success")
                    refresh()
                else:
                    socketio.emit("error_url")
            except Exception as e:
                save_error(e)
        else:
            socketio.emit("error_wifi")
    except Exception as e:
        save_error(e)    

@socketio.on('new-prayertime-salahtimes2')
def new_prayertime_salahtimes2(json):
    try:
        if internet_on():
            print(DeleteTable("prayertimes"))
            print(CreateTable( "prayertimes" ))
            id = int(json["data"])
            get_prayertime_vaktija( id )
            refresh()
        else:
            socketio.emit("error_wifi")
    except Exception as e:
        save_error(e)  

@socketio.on('new-prayertime-vaktijaeu')
def new_prayertime_salahtimes2(json):
    try:
        if internet_on():
            slug  = str(json["data"])
            prayer_times = check_vaktija_eu(slug)
            print(prayer_times)
            if prayer_times == False:
                socketio.emit("error_url")
            else:
                print(DeleteTable("prayertimes"))
                print(CreateTable( "prayertimes" ))
                get_prayertimes_vaktijaEU(slug)
                print(prayer_times)
                refresh()
        else:
            socketio.emit("error_wifi")
    except Exception as e:
        save_error(e)    
        
@socketio.on('rotate_screen')
def rotate_screen(json):
    try:
        rotation  = str(json["data"])
        rotation_command = f"xrandr -o {rotation}"
        rotation_autostart = "/etc/X11/Xsession.d/45custom_xrandr-settings"
        if os.path.exists(rotation_autostart) != True:
            subprocess.call(['sudo', 'touch', rotation_autostart])
            subprocess.call(['sudo', 'chmod', '777', rotation_autostart])
        with open(rotation_autostart, "w") as f:
            f.write(rotation_command)
        
        os.system("xrandr -o {}".format(rotation))
    except Exception as e:
        print(e)
        save_error(e)        
        
def refresh():
    try:
        socketio.emit("refresh")
    except:
        pass