
from prayerscreen import create_app, socketio
import os

app = create_app()

def check_internet():
    try:
        os.system('ping -c 1 google.com')
        return True
    except Exception:
        return False
    

if __name__ == '__main__':
    # Production
    # if check_internet():
    #     os.system('pip3 install -r requirements.txt')
    # socketio.run(app, host='0.0.0.0', debug=True, port=80)
    
    # Development
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
        

