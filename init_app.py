#RUN ONLY IF YOU ARE ON LINUX

import os

os.system('sudo apt install authbind')
os.system('sudo touch /etc/authbind/byport/80')
os.system('sudo chmod 777 /etc/authbind/byport/80')


#Run programm after with this command
# authbind --deep python3 app.py