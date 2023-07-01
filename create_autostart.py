import os, sys
#----------- Create file Autostart ----------- 
path_to_this_folder = os.getcwd()
path_to_desktop = "prayertime_autostart.sh"
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
def get_user_config_directory():
    """Returns a platform-specific root directory for user config settings."""
    # On Windows, prefer %LOCALAPPDATA%, then %APPDATA%, since we can expect the
    # AppData directories to be ACLed to be visible only to the user and admin
    # users (https://stackoverflow.com/a/7617601/1179226). If neither is set,
    # return None instead of falling back to something that may be world-readable.
    if os.name == "nt":
        appdata = os.getenv("LOCALAPPDATA")
        if appdata:
            return appdata
        appdata = os.getenv("APPDATA")
        if appdata:
            return appdata
        return None
    # On non-windows, use XDG_CONFIG_HOME if set, else default to ~/.config.
    xdg_config_home = os.getenv("XDG_CONFIG_HOME")
    if xdg_config_home:
        return xdg_config_home
    return os.path.join(os.path.expanduser("~"), ".config") 

path_to_autostart_folder = str(get_user_config_directory()) + "/autostart"

try:
    os.mkdir(path_to_autostart_folder)
except OSError:
    print ("Creation of the directory %s failed" % path_to_autostart_folder)
else:
    print ("Successfully created the directory %s " % path_to_autostart_folder)

path_to_autostart = str(get_user_config_directory()) + "/autostart/prayertime_autostart.desktop" 
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

print("\n\n\n\nAUTOSTART DONE\n\n\n\n")
