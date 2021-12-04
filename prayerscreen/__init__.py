from flask import Flask
from flask_socketio import SocketIO, emit
from prayerscreen.config import Config 
from flask_sqlalchemy import SQLAlchemy


# Initialize socketio
socketio = SocketIO()

#initialize database
db = SQLAlchemy()

def create_app(config_class=Config):
    #Create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # Configure routes
    from prayerscreen.main.routes import main
    app.register_blueprint(main)
    

    socketio.init_app(app)

    return  app