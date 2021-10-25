import requests
from bs4 import BeautifulSoup as soup
import datetime
import sqlite3
import csv 
import json


def internet_on():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False
        
def NewPrayerTime( url , country , city):
    try:
        now = datetime.datetime.now()
        this_year = str(now.year)
        year_after = str(now.year + 5)
        headers = {'content-Type': 'application/json', "user-Agent" : "Mozilla/5.0"}
        data = {
            "start":"01 Jan "+this_year+"",
            "end":"31 Dec "+year_after+"",
            "placeUniqueName":""+str(city)+"",
            "countryUniqueName": ""+str(country)+"",
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
                    current_date = str(current_year) + "-" + str(current_moth)
                    
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
                    one_day_prayertime.append(current_date + "-" +  current_day)
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
    
def CheckDatabase(table):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM "+ str(table))
        print(c.fetchall())
    except:
        print("There is no table with this name: "+ table)

def DeleteTable( table ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DROP TABLE "+ str(table))
        conn.commit()
        conn.close()
        return True
    except:
        return False

def CreateTable( table ):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE "+str(table) +" (date text, fajr text, sunrise text, dhuhr text, asr text, maghrib text, isha text)")
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
def CheckURL(url):
    request = requests.get(url)
    if request.status_code == 200:
        return True
    else:
        return False
    
    
def Check_CSV_prayertimes( path ):
    error_list = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        first_row = False
        for row in csv_reader:
            if first_row != False:
                    
                datum = row[0]
                if len(datum) != 10 and len(datum) != 5:
                    print(datum)
                    error_list.append(str(row))
                    
                if len(datum) == 5:
                    datum = datum.replace(datum[2], ":")
                fajr = row[1]
                sunrise = row[2]
                dhuhr = row[3]
                asr = row[4]
                maghrib = row[5]
                isha = row[6]
                
                if len(fajr) != 5 and len(sunrise) != 5 and len(dhuhr) != 5 and len(asr) != 5  and len(maghrib) != 5  and len(isha) != 5:
                    error_list.append(str(row))
            else:
                first_row = True
        
    return error_list
    
def CSV_prayertimes( path ):
    """Add to database prayertimes from CSV file

    Args:
        path (String): [Path to file]
    """    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        first_row = False
        for row in csv_reader:
            if first_row != False:      
                datum = row[0]
                fajr = row[1]
                sunrise = row[2]
                dhuhr = row[3]
                asr = row[4]
                maghrib = row[5]
                isha = row[6]
                c.execute("INSERT INTO prayertimes VALUES ( ? , ? , ? , ? , ? , ? , ?)", (datum,fajr, sunrise, dhuhr, asr, maghrib, isha))
            else:
                first_row = True
    conn.commit()
    conn.close()
     

def get_prayertime_vaktija( id ):
    """[Get prayertime from vakrija.ba 5 YEARS]

    Args:
        id ([int]): [City ID you can find it here https://api.vaktija.ba/vaktija/v1]
    """    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    try:
        now = datetime.datetime.now()
        this_year = now.year
        year_after = now.year + 5
        for year in range(this_year, year_after):
            url = "https://api.vaktija.ba/vaktija/v1/"+str(id)+"/"+str(year)+""
            res = requests.get(url)
            res_json = json.loads(res.text)
            all_year = res_json["mjesec"]
            #loop thru months
            count  = 0
            for month in all_year:
                count += 1
                #loop thru days
                count2 = 0
                for day in month["dan"]:
                    count2 += 1
                    
                    string_month = str(count)
                    string_day = str(count2)

                    if len(string_month) == 1 and len(string_day) == 1: 
                        date = ""+str(year)+"-0"+str(string_month)+"-0"+str(string_day) + ""
                    elif len(string_month) == 1 and len(string_day) != 1: 
                        date = ""+str(year)+"-0"+str(string_month)+"-"+str(string_day) + ""
                    elif len(string_month) != 1 and len(string_day) == 1: 
                        date = ""+str(year)+"-"+str(string_month)+"-0"+str(string_day) + ""  
                    elif len(string_month) != 1 and len(string_day) != 1: 
                        date = ""+str(year)+"-"+str(string_month)+"-"+str(string_day) + ""      
                    

                    prayertimes = day["vakat"]
                    if len(prayertimes[0]) == 4:
                        prayertimes[0] = "0"+prayertimes[0] 
                    if len(prayertimes[1]) == 4:
                        prayertimes[1] = "0"+prayertimes[1] 

                    c.execute("INSERT INTO prayertimes VALUES ( ? , ? , ? , ? , ? , ? , ?)", (date,day["vakat"][0],day["vakat"][1],day["vakat"][2],day["vakat"][3],day["vakat"][4],day["vakat"][5]))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)       
    
def get_prayertimes_vaktijaEU( location_slug ):
    url = "https://api.vaktija.eu/v1/locations/slug/" + location_slug
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    res_json = requests.get(url).json()
    months =  res_json["data"]["months"]
    current_year = str(datetime.date.today().year)

    for month in months:
        current_month = "0" + str(month) if len(month) == 1 else month
        for days in months[month]:
            for day in months[month]["days"]:
                current_day = "0" + str(day) if len(day) == 1 else day
                current_date =f"{current_year}-{current_month}-{current_day}"
                the_prayertimes = months[month]["days"][day]["prayers"]
                if len(the_prayertimes) != 0 :
                        h = current_date,the_prayertimes[0],the_prayertimes[1],the_prayertimes[2],the_prayertimes[3],the_prayertimes[4],the_prayertimes[5]
                        c.execute("INSERT INTO prayertimes VALUES ( ? , ? , ? , ? , ? , ? , ?)", (current_date,the_prayertimes[0],the_prayertimes[1],the_prayertimes[2],the_prayertimes[3],the_prayertimes[4],the_prayertimes[5]))
                
    conn.commit()
    conn.close()

def check_vaktija_eu( location_slug ):
    url = "https://api.vaktija.eu/v1/locations/slug/" + location_slug
    try:
        res_json = requests.get(url).json()
        months =  res_json["data"]["months"]
        current_year = str(datetime.date.today().year)

        for month in months:
            current_month = "0" + str(month) if len(month) == 1 else month
            for days in months[month]:
                for day in months[month]["days"]:
                    current_day = "0" + str(day) if len(day) == 1 else day
                    current_date =f"{current_year}-{current_month}-{current_day}"
                    the_prayertimes = months[month]["days"][day]["prayers"]
                    h = current_date,the_prayertimes[0],the_prayertimes[1],the_prayertimes[2],the_prayertimes[3],the_prayertimes[4],the_prayertimes[5]
                    print(h)
                    return True
    except Exception as e:
        print(e)
        return False
if __name__ == "__main__":
    pass
    # print(DeleteTable("prayertimes"))
    # print(CreateTable( "prayertimes" ))
    # NewPrayerTime( "https://www.salahtimes.com/sweden/stockholm/render" )
    # CheckDatabase("prayertimes")
    # print(CheckURL("https://www.salahtimes.com/sweden/gothenburg/render"))
    print(Check_CSV_prayertimes( "./static/upload/BHA.csv" ))
