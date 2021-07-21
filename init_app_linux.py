#----------------------------------------------------------------


#RUN ONLY IF YOU ARE ON LINUX


#----------------------------------------------------------------

import os, sys
if not 'SUDO_UID' in os.environ.keys():
    print("Run program as ROOT!")

# ----------- Update system ----------- 
os.system("sudo apt update;")

# ----------- Install pip -----------  
os.system("sudo apt install python3-pip -y;pip3 install -r requirements.txt;")

# ----------- Install Firefox ----------- 
os.system("sudo apt install firefox-esr -y;")

# ----------- Install ScreenSaver ----------- 
os.system("sudo apt install xscreensaver -y;")

# ----------- Install Authbind ----------- 
os.system('sudo apt install authbind -y;sudo touch /etc/authbind/byport/80;sudo chmod 777 /etc/authbind/byport/80;')

# ----------- Install Authbind ----------- 
os.system('sudo apt install authbind -y;sudo touch /etc/authbind/byport/80;sudo chmod 777 /etc/authbind/byport/80;')

# ----------- DONE ----------- 
print("\nDONE\n")