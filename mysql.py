import sqlite3
from help_functions import *

conn = sqlite3.connect("database.db")
c = conn.cursor()

#Add columt to table
# c.execute("""ALTER TABLE settings ADD id INTEGER """)

#Update data in table
# c.execute("""UPDATE settings SET iqamah_on = 'true' WHERE id = 1 """)
# conn.commit()
# c.execute("""select * from settings """)
c.execute("""select iqamah_on from settings where id = 1 """)

res = c.fetchone()[0]
print(res)

# c.execute("""select fajr, dhuhr, asr, maghrib, isha from prayertimes where date = '2021-06-13' """)
# prayer_times = c.fetchall()[0]

# c.execute("""select fajr_iqamah, dhuhr_iqamah, asr_iqamah text, maghrib_iqamah, isha_iqamah from settings""")
# all_iqamah = c.fetchall()[0]

# fajr_iqamah = add_minutes_to_time(str(prayer_times[0]), int(all_iqamah[0]))
# dhuhr_iqamah = add_minutes_to_time(str(prayer_times[1]), int(all_iqamah[1]))
# asr_iqamah = add_minutes_to_time(str(prayer_times[2]), int(all_iqamah[2]))
# maghrib_iqamah = add_minutes_to_time(str(prayer_times[3]), int(all_iqamah[3]))
# isha_iqamah = add_minutes_to_time(str(prayer_times[4]), int(all_iqamah[4]))    
