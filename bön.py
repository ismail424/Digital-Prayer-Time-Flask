import csv 
from datetime import datetime
from datetime import timedelta

def bönbön():
    datum = datetime.today().strftime('%m-%d')
    with open('GBG.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if datum == row[0]:
                dagensbön = row

    fajr = dagensbön[1]
    fajriqamah = dagensbön[2]
    solupgång = dagensbön[3]
    zuhr = dagensbön[4]
    zuhriqamah = dagensbön[5]
    asr = dagensbön[6]
    asriqamah = dagensbön[8]
    magrib = dagensbön[9]
    magribiqamah = dagensbön [10]
    isha = dagensbön[11]        
    ishaiqamah = dagensbön[12]
    dag = datum
    
    datum = datetime.now() + timedelta(days=1)
    datum = datum.strftime('%m-%d')
    with open('GBG.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if datum == row[0]:
                dagensbön = row
            else:
                fajrimon = "06:53"

    fajrimon = dagensbön[1]

    return(fajrimon,dag,fajr,fajriqamah,solupgång,zuhr,zuhriqamah,asr,asriqamah,magrib, magribiqamah,isha,ishaiqamah)

# fajr = dagensbön[1]
# fajr = datetime.strptime(fajr, '%H:%M')
# minutes_to_add = 10
# fajriq = fajr + timedelta(minutes = minutes_to_add)
# print(fajriq.time())