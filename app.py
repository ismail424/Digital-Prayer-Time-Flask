from flask import Flask, render_template, request,redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)

#This secret key dosen't do anything but you need this!
app.config[ 'SECRET_KEY' ] = 'Secret key'
socketio = SocketIO( app )

@app.route( '/' )
def start():
  return render_template( 'start.html' )


@socketio.on( 'event' )
def event( json ):
  socketio.emit( 'event', json )


if __name__ == '__main__':

  #Debug only
  socketio.run( app, debug = True )

  #Server på LAN
  # socketio.run(app, host='0.0.0.0')
