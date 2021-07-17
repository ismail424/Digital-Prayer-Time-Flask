#RUN ONLY IF YOU ARE ON LINUX
import os

#Update system
os.system("sudo apt update;")

#Install pip / 
os.system("sudo apt install python3-pip -y;pip install -r requirements.txt;")

#Install Firefox
os.system("sudo apt install firefox-esr -y;")

#Install ScreenSaver
os.system("sudo apt install xscreensaver -y;")

#Install Authbind
os.system('sudo apt install authbind -y;sudo touch /etc/authbind/byport/80;sudo chmod 777 /etc/authbind/byport/80;')


#Run programm after with this command
# authbind --deep python3 app.py