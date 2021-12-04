#----------------------------------------------------------------


#RUN ONLY IF YOU ARE ON LINUX


#----------------------------------------------------------------

import os

# ----------- Update system ----------- 
os.system("sudo apt update -y;")

# ----------- Install pip -----------  
os.system("sudo apt install python3-pip -y;pip3 install -r requirements.txt;")

# ----------- Install Firefox ----------- 
os.system("sudo apt install firefox-esr -y;")

# ----------- Install ScreenSaver ----------- 
os.system("sudo apt install xscreensaver -y;")

# ----------- Remove apache2 / nginx -----------
os.system("sudo apt remove apache2 -y;sudo apt remove nginx -y;")

# ----------- Install Authbind ----------- 
os.system('sudo apt install authbind -y;sudo touch /etc/authbind/byport/80;sudo chmod 777 /etc/authbind/byport/80;')

#----------- Create file Autostart ----------- 
path_to_this_folder = os.getcwd()
path_to_autostartSH = str(os.path.expanduser("~")) + "/prayertime_autostart.sh"
path_to_appfile = path_to_this_folder + "/app.py"
autostart_string = """ #!/bin/bash
cd {};
authbind python3 app.py &
firefox -kiosk http://0.0.0.0/prayerscreen
""".format(path_to_this_folder)

try:
    with open(path_to_autostartSH, "w") as f:
        f.write(autostart_string)        
    chmod_string = "chmod +x {}".format(path_to_autostartSH)
    os.system(chmod_string)
except:
    print("Error creating autostart file (prayertime_autostart.sh)\nTry to run this script again.")
    os._exit(1)

# ----------- Create file Autostart.desktop ----------- 
home_config_dir = os.path.join(os.path.expanduser("~"), ".config") 
path_to_autostart_folder = str(home_config_dir) + "/autostart"

try:
    os.mkdir(path_to_autostart_folder)
except OSError:
    print ("Creation of the autostart directory failed")

path_to_autostart = str(home_config_dir) + "/autostart/prayertime_autostart.desktop" 
desktopfile_string = """[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=<GUI Controller>
Exec= {}
StartupNotify=false
Terminal=true
Hidden=false
""".format(path_to_autostartSH)
try:
    with open(path_to_autostart, "w") as f:
        f.write(desktopfile_string)
    chmod2_string = "chmod +x {}".format(path_to_autostart)
    os.system(chmod2_string)
except:
    print("\n\nCant write autostart.desktop to the autostart directory\n\n")
    

print("\n\n\n\nDONE\n\n\n\n")