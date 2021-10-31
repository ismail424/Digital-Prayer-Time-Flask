#!/bin/bash
sudo apt remove apache2 -y;
sudo apt remove nginx -y;
sudo python3 init_app_linux.py;
python3 create_autostart.py;
authbind python3 app.py &
firefox "http://0.0.0.0";
