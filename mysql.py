import sqlite3
from help_functions import *

conn = sqlite3.connect("database.db")
c = conn.cursor()


# c.execute("CREATE TABLE translate (monday text,tuesday text,wednesday text,thursday text,friday text,saturday text,sunday text,prayer text,begins text,iqamah text, fajr text, sunrise text, dhuhr text, asr text, maghrib text, isha text, next_text text, footer_text text)")
# conn.commit()


# c.execute("CREATE TABLE images (url_1 text, url_2 text, google_slide_url text, video_url text, current_select text, slide_delay text)")
# conn.commit()

# translate_key = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
#              "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next_text" , "footer_text" ]
# # for x in translate_key:
# #     print(x + "= '{}', ", end = '')

# translate = ["monday" ,"tuesday" ,"wednesday" ,"thursday" ,"friday" ,"saturday" ,"sunday" ,"prayer" ,"begins" ,"iqamah" , "fajr" , 
#              "sunrise" , "dhuhr" , "asr" , "maghrib" , "isha" , "next" , "Please, turn off your phones" ]
# c.execute("INSERT INTO translate VALUES ( ? , ? , ? , ? , ? , ? , ? ,? , ? , ? , ? , ? , ? , ?, ? ,? , ?, ?)", (translate))
# c.execute(" DELETE FROM translate ")

# c.execute("INSERT INTO images VALUES ( '' , '' , '' , '', 'none' , '30' )")
# conn.commit()


# Add columt to table
# c.execute("""ALTER TABLE settings ADD fajr_iqamah_before_sunrise text """)
# conn.commit()

#Rename
# c.execute("""ALTER TABLE settings RENAME fajr_iqamah_after_sunrise TO fajr_iqamah_before_sunrise """)
# conn.commit()

#Update data in table
# c.execute("""UPDATE translate SET monday= '{}', tuesday= '{}', wednesday= '{}', thursday= '{}', friday= '{}', saturday= '{}', sunday= '{}', prayer= '{}', begins= '{}', iqamah= '{}', fajr= '{}', sunrise= '{}', dhuhr= '{}', asr= '{}', maghrib= '{}', isha= '{}', next_text= '{}', footer_text= '{}' """.format(*translate))
# conn.commit()
# #c.execute("""select iqamah_on from settings where id = 1 """)

#Update data in table 2
# c.execute("""UPDATE settings SET fajr_iqamah_before_sunrise = 'false' """)
# conn.commit()


# c.execute("""select * from images """)
# res = c.fetchall()
# print(res)



# c.execute("""SELECT iqamah_on
# FROM settings""")
# res = c.fetchone()
# print(res)

# c.execute("""select fajr, dhuhr, asr, maghrib, isha from prayertimes where date = '2021-06-13' """)
# prayer_times = c.fetchall()[0]

# c.execute("""select fajr_iqamah, dhuhr_iqamah, asr_iqamah text, maghrib_iqamah, isha_iqamah from settings""")
# all_iqamah = c.fetchall()[0]

# fajr_iqamah = add_minutes_to_time(str(prayer_times[0]), int(all_iqamah[0]))
# dhuhr_iqamah = add_minutes_to_time(str(prayer_times[1]), int(all_iqamah[1]))
# asr_iqamah = add_minutes_to_time(str(prayer_times[2]), int(all_iqamah[2]))
# maghrib_iqamah = add_minutes_to_time(str(prayer_times[3]), int(all_iqamah[3]))
# isha_iqamah = add_minutes_to_time(str(prayer_times[4]), int(all_iqamah[4]))    
