#Import SQL
import sqlite3

#import time/date
import time
import  datetime

#import json
import json

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
        prayer_api.append("false")
        prayer_api_key = ["date", "fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha", "fajr_tomorrow", "error"]
        
        #Bind key to value (Convert list to dict)
        prayer_api = dict(zip(prayer_api_key,prayer_api))
        
        #Convert to json and return
        prayer_api = json.dumps(prayer_api)
        return prayer_api
    except:
        #If there is a error
        prayer_api_key = ["date", "fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha", "fajr_tomorrow", "error"]
        prayer_api_value = ["0000-00-00", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00", "00:00", "true"]
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
        print(e)
        return str(time)
            
if __name__ == '__main__':
    # print(get_prayertime_api())
    print(add_minutes_to_time("19:20", 40))
    pass