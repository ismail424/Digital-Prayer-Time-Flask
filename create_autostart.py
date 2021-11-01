import os, sys
#----------- Create file Autostart ----------- 
path_to_this_folder = os.getcwd()
path_to_desktop = str(os.path.expanduser("~/Desktop")) + "/prayertime_autostart.sh"
path_to_appfile = path_to_this_folder + "/app.py"
autostart_string = """#!/bin/bash
cd {};
authbind python3 app.py &
firefox -kiosk http://0.0.0.0/prayerscreen
""".format(path_to_this_folder)

try:
    with open(path_to_desktop, "w") as f:
        f.write(autostart_string)
except:
    path_to_desktop = str(os.path.expanduser("~")) + "/prayertime_autostart.sh"
    with open(path_to_desktop, "w") as f:
        f.write(autostart_string)
        
chmod_string = "chmod +x {}".format(path_to_desktop)
os.system(chmod_string)
     
     
# ----------- Create file Autostart.desktop ----------- 
path_to_autostart = str(os.path.expanduser("/.config/autostart")) + "/prayertime_autostart.desktop" 
desktopfile_string = """[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=<GUI Controller>
Exec= {}
StartupNotify=false
Terminal=true
Hidden=false
""".format(path_to_desktop)
try:
    with open(path_to_autostart, "w") as f:
        f.write(desktopfile_string)
except:
    print("\n\nCant create autostart.desktop\n\n")
    
chmod2_string = "chmod +x {}".format(path_to_autostart)
os.system(chmod2_string)
