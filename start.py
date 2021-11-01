import os, sys

autostart_string = """
authbind python3 app.py &
firefox -kiosk http://0.0.0.0/prayerscreen;
"""

os.system(autostart_string)