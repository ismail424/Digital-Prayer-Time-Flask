#!/bin/bash

# Disable screen blanking
disable_screen_blanking() {
    local config_file="/etc/lightdm/lightdm.conf"

    if [ ! -f "$config_file" ]; then
        echo "The LightDM configuration file does not exist. Creating file and applying settings."
        echo "[Seat:*]" | sudo tee $config_file > /dev/null
    fi

    local disable_blanking="xserver-command=X -s 0 dpms"

    if ! grep -q "$disable_blanking" $config_file; then
        echo "Adding settings to disable screen blanking..."
        echo "$disable_blanking" | sudo tee -a $config_file > /dev/null
    else
        echo "Settings already present in $config_file."
    fi

    echo "Please restart the LightDM service for changes to take effect."
    echo "You can restart LightDM by running: sudo systemctl restart lightdm"
}

# Remove web servers
remove_web_servers() {
    echo "Removing Apache2 and Nginx web servers..."
    sudo apt-get remove apache2 nginx -y
}

# Cleanup Python settings
cleanup_python() {
    local py_ext_path="/usr/lib/python3.*/EXTERNALLY-MANAGED"
    if [ -f $py_ext_path ]; then
        echo "Removing externally managed Python settings..."
        sudo rm $py_ext_path
    else
        echo "No externally managed Python settings found."
    fi
}

# Initialize and start application
start_application() {
    echo "Initializing and starting the application..."
    sudo python3 init_app_linux.py
    python3 create_autostart.py
    authbind python3 app.py &
    echo "Application started."
}

# Open web interface
open_web_interface() {
    echo "Opening web interface..."
    firefox http://0.0.0.0/ &
}

# Main function to control flow
main() {
    disable_screen_blanking
    remove_web_servers
    cleanup_python
    start_application
    open_web_interface
}

# Call main function
main
