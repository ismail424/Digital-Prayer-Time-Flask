from flask import Flask, send_from_directory
from flask.helpers import url_for
from flask_socketio import SocketIO, emit
from prayerscreen.config import Config 
from flask_sqlalchemy import SQLAlchemy
import os


# Initialize socketio
socketio = SocketIO()

#initialize database
db = SQLAlchemy()

def create_app(config_class=Config):

    #Create and configure the app    
    app = Flask(__name__, static_folder="./build_react")
    app.config.from_object(Config)
    db.init_app(app)
    
    # Configure routes (/api)
    from prayerscreen.main_api.routes_api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    
    # Serve React App
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    # Configure socketio
    socketio.init_app(app)

    return app