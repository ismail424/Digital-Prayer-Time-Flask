import requests
from bs4 import BeautifulSoup as soup
import datetime
import sqlite3

def internet_on():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False
        
def NewPrayerTime( url ):
    try:
        now = datetime.datetime.now()
        this_year = str(now.year)
        year_after = str(now.year + 3)
        headers = {'content-Type': 'application/json', "user-Agent" : "Mozilla/5.0"}
        data = {
            "start":"01 Jan "+this_year+"",
            "end":"31 Dec "+year_after+"",
            "placeUniqueName":"gothenburg",
            "countryUniqueName":"sweden",
            "asarCalculationMethod":2,
            "prayerCalculationMethod":1,
            "highLatitudeMethod":4,
            "dateRangeType":4,
            "areRamadanTimes":False
            }
        r = requests.post(url, headers= headers, json=data)
    except:
        return False

    r_text = r.text
    r_html = soup(r_text, "html.parser")
    all_td = r_html.findAll("td")
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    one_day_prayertime = []
    
    for td in all_td:
        #Fetches all the moths
        if td.span != None:
            count = 0
            for span in td:
                if count == 3:
                    current_moth = span.text.split()[0]
                    current_year = span.text.split()[1]
                    if current_moth == "Jan":
                        current_moth = "01"
                    elif current_moth == "Feb":
                        current_moth = "02"
                    elif current_moth == "Mar":
                        current_moth = "03"
                    elif current_moth == "Apr":
                        current_moth = "04"
                    elif current_moth == "May":
                        current_moth = "05"
                    elif current_moth == "Jun":
                        current_moth = "06"
                    elif current_moth == "Jul":
                        current_moth = "07"
                    elif current_moth == "Aug":
                        current_moth = "08"
                    elif current_moth == "Sep":
                        current_moth = "09"
                    elif current_moth == "Oct":
                        current_moth = "10"
                    elif current_moth == "Nov":
                        current_moth = "11"
                    elif current_moth == "Dec":
                        current_moth = "12"
                
                    current_date = str(current_year) + "/" + str(current_moth)
                count += 1
        
        #Fetches every prayertime 
        else:
                        
            prayer_text = td.text.split()
            try:
                if prayer_text[1] != None:
                    if len(one_day_prayertime) == 7:
                        c.execute("INSERT INTO prayertimes VALUES ( ? , ? , ? , ? , ? , ? , ?)", (one_day_prayertime))
                        
                    one_day_prayertime = []
                    current_day = str(prayer_text[1])
                    if len(current_day)  == 1:
                        current_day = "0"+ current_day
                    one_day_prayertime.append(current_date + "/" +  current_day)
                    x = 0
            except:
                if prayer_text[0] != "Day":
                    if prayer_text[0] != "Fajr":
                        if prayer_text[0] != "Sunrise":
                            if prayer_text[0] != "Dhuhr":
                                if prayer_text[0] != "Asr":
                                    if prayer_text[0] != "Maghrib":
                                        if prayer_text[0] != "Isha":
                                            if x == 0:
                                                this_prayer = "0" + prayer_text[0] 
                                                one_day_prayertime.append(this_prayer)
                                            elif x == 1:
                                                this_prayer = "0" + prayer_text[0] 
                                                one_day_prayertime.append(this_prayer)
                                            elif x == 2:
                                                this_prayer = prayer_text[0] 
                                                this_prayer = fixTime(this_prayer)
                                                one_day_prayertime.append(this_prayer)

                                            elif x == 3:
                                                this_prayer = prayer_text[0] 
                                                this_prayer = fixTime(this_prayer)
                                                one_day_prayertime.append(this_prayer)
                                            elif x == 4 :
                                                this_prayer = prayer_text[0] 
                                                this_prayer = ForcefixTime(this_prayer)
                                                one_day_prayertime.append(this_prayer)
                                            elif x == 5 :
                                                this_prayer = prayer_text[0] 
                                                this_prayer = ForcefixTime(this_prayer)
                                                one_day_prayertime.append(this_prayer)

                                            x += 1
    conn.commit()
    conn.close()
    
def fixTime( time ):
    if len(time) == 4:
        if time[0] == "1":
            time = "13"+ time[1:]
        if time[0] == "2":
            time = "14"+ time[1:]
        if time[0] == "3":
            time = "15"+ time[1:]
        if time[0] == "4":
            time = "16"+ time[1:]
        if time[0] == "5":
            time = "17"+ time[1:]
        if time[0] == "6":
            time = "18"+ time[1:]
        if time[0] == "7":
            time = "19"+ time[1:]
        if time[0] == "8":
            time = "20"+ time[1:]
        if time[0] == "9":
            time = "21"+ time[1:]
        if time[0] == "10":
            time = "22"+ time[1:]
        if time[0] == "11":
            time = "23"+ time[1:]
        if time[0] == "12":
            time = "00"+ time[1:]
        return time
    else:
        return time
def ForcefixTime( time ):
    if len(time) == 4:
        if time[0] == "1":
            time = "13"+ time[1:]
        if time[0] == "2":
            time = "14"+ time[1:]
        if time[0] == "3":
            time = "15"+ time[1:]
        if time[0] == "4":
            time = "16"+ time[1:]
        if time[0] == "5":
            time = "17"+ time[1:]
        if time[0] == "6":
            time = "18"+ time[1:]
        if time[0] == "7":
            time = "19"+ time[1:]
        if time[0] == "8":
            time = "20"+ time[1:]
        if time[0] == "9":
            time = "21"+ time[1:]
        if time[0] == "10":
            time = "22"+ time[1:]
        if time[0] == "11":
            time = "23"+ time[1:]
        if time[0] == "12":
            time = "00"+ time[1:]
        return time
    else:
        
        if time[0:2] == "10":
            time = "22"+ time[2:]
        if time[0:2] == "11":
            time = "23"+ time[2:]
        if time[0:2] == "12":
            time = "00"+ time[2:]
        return time
    
def CheckDatabase( table):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM "+ str(table))
        print(c.fetchall())
    except:
        print("There is no table with this name: "+ table)

def deleteTable( table ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DROP TABLE "+ str(table))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def createTable( table ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE "+str(table) +" (date text, fajr text, sunrise text, dhuhr text, asr text, maghrib text, isha text)")
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
if __name__ == "__main__":
    # print(deleteTable("prayertimes"))
    # NewPrayerTime( "https://www.salahtimes.com/sweden/gothenburg/render" )
    # print(createTable( "prayertimes" ))
    # CheckDatabase("prayertimes")
    pass