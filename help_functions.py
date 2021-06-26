#Import SQL
import sqlite3

#import time/date
import time
import  datetime

#import json
import json

#import sys
import sys
import time
import os

#Description:This function will return the prayertimes for today and fajr time for tomorrow! 
#Argument 1: klass - None
#Return: klass - JSON (ALl the prayertimes for the prayertime screen (Today prayertimes and Fajr time for tomorrow))
#By: Ismail Sacic
#Date: 2021-06-12
def get_prayertime_api():
    try:
        #Get the date
        today = str(datetime.date.today())
        tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
        
        #Connect to the database
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        
        #MySQL QUERY
        c.execute("""SELECT * FROM prayertimes WHERE date = '{}' """.format(today))
        #Fetch the row and save it to a variable
        today_prayertimes = c.fetchone()
        if today_prayertimes == None:
            c.execute("""SELECT * FROM prayertimes WHERE date LIKE '%{}%' """.format(today))
            today_prayertimes = c.fetchone()
            if today_prayertimes == None:
                today = str(datetime.date.today())
                today = today[5:]
                c.execute("""SELECT * FROM prayertimes WHERE date LIKE '%{}%' """.format(today))
                today_prayertimes = c.fetchone()        
                    
        today_prayertimes = list(today_prayertimes)

        
        #MySQL QUERY
        c.execute("""SELECT * FROM prayertimes WHERE date = '{}' """.format(tomorrow))
        #Fetch the row and save it to a variable
        tomorrow_prayertimes = c.fetchone()
        if tomorrow_prayertimes == None:
            c.execute("""SELECT * FROM prayertimes WHERE date like '%{}%' """.format(tomorrow))
            tomorrow_prayertimes = c.fetchone()
            if tomorrow_prayertimes == None:
                tomorrow = tomorrow[5:]
                c.execute("""SELECT * FROM prayertimes WHERE date like '%{}%' """.format(tomorrow))
                tomorrow_prayertimes = c.fetchone()
                
        tomorrow_prayertimes = list(tomorrow_prayertimes)
        fajr_time = tomorrow_prayertimes[1]
        
        #ADD the two list together in a array
        prayer_api = today_prayertimes
        prayer_api.append(fajr_time)
        prayer_api.append(("false").lower())
        prayer_api.append(check_iqamah().lower())
        prayer_api.extend(calculate_iqamah( today ))
        
        c.execute("""SELECT isha_fixed FROM settings""")
        isha_fixed = c.fetchone()[0]
        
        if isha_fixed != "0":
            if len(isha_fixed) == 5:
                prayer_api[6] = isha_fixed
                prayer_api[14] = isha_fixed
        
        prayer_api_key = ["date", "fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha", "fajr_tomorrow", "error","iqamah_on","fajr_iqamah", "dhuhr_iqamah", "asr_iqamah", "maghrib_iqamah", "isha_iqamah"]
        
        #Bind key to value (Convert list to dict)
        prayer_api = dict(zip(prayer_api_key,prayer_api))
        
        #Convert to json and return
        prayer_api = json.dumps(prayer_api)
        return prayer_api
    except:
        #If there is a error
        prayer_api_key = ["date", "fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha", "fajr_tomorrow", "error","iqamah_on","fajr_iqamah", "dhuhr_iqamah", "asr_iqamah", "maghrib_iqamah", "isha_iqamah"]
        prayer_api_value = ["0000-00-00", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00", "true", "false","00:00", "00:00", "00:00", "00:00", "00:00"]
        prayer_api = dict(zip(prayer_api_key,prayer_api_value))
        prayer_api = json.dumps(prayer_api)
        return prayer_api
        
def add_minutes_to_time( time , minutes ):
    try:
        #Konverterar string till time format och lägger till tid
        time = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes = minutes)
        time = str(datetime.datetime.strftime(time, "%H:%M"))
        return time
    except Exception as e: 
        save_error(e)
        try:
            with open("error.txt", "a") as f:
                f.write(str(e)+"\n\n")
        except:
            pass
        return str(time)

#This will return if the user wants iqamah or not, It will return true if iqamah is on and false if iqamah is off    
def check_iqamah():
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""select iqamah_on from settings where id = 1 """)
        res = c.fetchone()[0]
        if  res.lower() == "true":
            return "true"
        else:
            return "false"
    except:
        return "false"

    
def calculate_iqamah( date ):
    try:
        date = str(date)
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("""select fajr, dhuhr, asr, maghrib, isha, sunrise from prayertimes where date = '{}' """.format(date))
        prayer_times = c.fetchone()

        c.execute("""select fajr_iqamah, dhuhr_iqamah, asr_iqamah , maghrib_iqamah, isha_iqamah,fajr_iqamah_before_sunrise from settings""")
        all_iqamah = c.fetchone()

        if all_iqamah[5] == "false":
            fajr_iqamah = add_minutes_to_time(str(prayer_times[0]), int(all_iqamah[0]))
        else:
            sunrise = str(prayer_times[5])
            iqamah_fajr = int(all_iqamah[0]) * -1
            fajr_iqamah = add_minutes_to_time(sunrise,iqamah_fajr)
        dhuhr_iqamah = add_minutes_to_time(str(prayer_times[1]), int(all_iqamah[1]))
        asr_iqamah = add_minutes_to_time(str(prayer_times[2]), int(all_iqamah[2]))
        maghrib_iqamah = add_minutes_to_time(str(prayer_times[3]), int(all_iqamah[3]))
        isha_iqamah = add_minutes_to_time(str(prayer_times[4]), int(all_iqamah[4]))    
        
        final_list = [fajr_iqamah, dhuhr_iqamah, asr_iqamah, maghrib_iqamah, isha_iqamah]
        
        return final_list
    
    except Exception as e: 
        save_error(e)
        try:
            with open("error.txt", "a") as f:
                f.write(str(e)+"\n\n")
        except:
            pass
        return ["00:00", "00:00", "00:00", "00:00", "00:00"]
        
        
def get_translation_json():
    """[This function will return the translation settings in json format!]

    Returns:
        [json]: [keys and values for the translation]
    """    
    translate = get_translation()
    the_key_values = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
             "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next_text" , "footer_text" ]
    res = dict(zip(the_key_values, translate))
    
    res = json.dumps(res)
    
    return res
        
        
def get_translation():
    """This function returns the translation list from the database

    Returns:
        [list]: [Translation from database (table:translation)]
    """    
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""select * from translate""")
        translate = list(c.fetchone())
        return translate
    except Exception as e: 
        save_error(e)
        translate = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
             "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next" , "Please, turn off your phones" ]
        return translate
                
def save_new_translate_values( translate_values_list ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""UPDATE translate SET monday= '{}', tuesday= '{}', wednesday= '{}', thursday= '{}', friday= '{}', saturday= '{}', sunday= '{}', prayer= '{}', begins= '{}', iqamah= '{}', fajr= '{}', sunrise= '{}', dhuhr= '{}', asr= '{}', maghrib= '{}', isha= '{}', next_text= '{}', footer_text= '{}' """.format(*translate_values_list))
        conn.commit()   
    except Exception as e:
        save_error(e)
        
def save_new_settings( settings_value_list ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""UPDATE settings SET iqamah_on = '{}',fajr_iqamah = '{}',fajr_iqamah_before_sunrise = '{}', dhuhr_iqamah = '{}', asr_iqamah = '{}', maghrib_iqamah= '{}', isha_iqamah= '{}', isha_fixed = '{}', qrcode= '{}'""".format(*settings_value_list))
        conn.commit()   
    except Exception as e:
        settings_value_list = ['ture','30', 'false', '10', '10', '0', '10', '0', 'true']
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""UPDATE settings SET iqamah_on = '{}',fajr_iqamah = '{}',fajr_iqamah_before_sunrise = '{}', dhuhr_iqamah = '{}', asr_iqamah = '{}', maghrib_iqamah= '{}', isha_iqamah= '{}', isha_fixed = '{}', qrcode= '{}'""".format(*settings_value_list))
        conn.commit()   
        save_error(e)
        
def get_settings():
    """Returns a dict with the current settings and their key values

    Returns:
        [dict]: Settings
    """    
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""select iqamah_on,fajr_iqamah,fajr_iqamah_before_sunrise, dhuhr_iqamah, asr_iqamah, maghrib_iqamah, isha_iqamah, isha_fixed, qrcode from settings""")
        settings = list(c.fetchone())        
        the_key_values = ["iqamah_on","fajr_iqamah" ,"fajr_iqamah_before_sunrise" ,"dhuhr_iqamah" ,"asr_iqamah" ,"maghrib_iqamah" ,"isha_iqamah" ,"isha_fixed" ,"qrcode" ]
        result = dict(zip(the_key_values, settings))
    
        return result
    except Exception as e:
        save_error(e)
        values = ['true','30', 'false', '10', '10', '0', '10', '0', 'true']
        the_key_values = ["iqamah_on","fajr_iqamah" ,"fajr_iqamah_before_sunrise" ,"dhuhr_iqamah" ,"asr_iqamah" ,"maghrib_iqamah" ,"isha_iqamah" ,"isha_fixed" ,"qrcode" ]
        result = dict(zip(the_key_values, values))
        
        return result
        
def save_new_images( value ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""UPDATE images SET url_1 = '{}', url_2= '{}',video_url ='{}',google_slide_url = '{}',current_select= '{}',slide_delay='{}'""".format(*value))
        conn.commit()   
    except Exception as e:
        value = ['','', '', '', 'none', '30']
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""UPDATE images SET url_1 = '{}', url_2= '{}', video_url ='{}', google_slide_url= '{}',current_select= '{}',slide_delay='{}'""".format(*value))
        conn.commit()   
        save_error(e)
        
     

def get_images():
    """Get current image settings from database

    Returns:
        [dict]: [Returns current image settings]
    """    
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""select * from images """)
        values = list(c.fetchone())
        the_key_values = ["url_1", "url_2", "google_slide_url","video_url","current_select","slide_delay"]
        result = dict(zip(the_key_values, values))
        return result
    
    except Exception as e:
        values = ['', '', '', '', 'images', '30']
        the_key_values = ["url_1", "url_2", "google_slide_url","video_url","current_select","slide_delay"]
        result = dict(zip(the_key_values, values))
        save_error(e)
        


def save_error( error ):
    try:
        error = 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(error).__name__, error
        error = str(error)
    except:
        error = str(error)
    today = datetime.date.today()
    date =  today.strftime("%Y-%m-%d")
    full_error = str(date) + " | "+ error  + "\n\n"
    with open("error.txt","a") as f:
        f.write(full_error)    

def sync_time():
    try:
        import ntplib
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        os.system('sudo date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
    except:
        print('Could not sync with time server.')

if __name__ == '__main__':
    # print(get_prayertime_api())
    # print(add_minutes_to_time("19:20", 40))
    # print(calculate_iqamah( "2021-06-13"))
    #print(check_iqamah())
    # print(get_translation_json())
    # add_minutes_to_time( "10" , 10 )
    sync_time()
    pass