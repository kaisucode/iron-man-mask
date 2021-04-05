
import socketio

URL = 'http://doranelle.kevinhsu.net:5000/websockets'
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('pi_do')
def pi_do(data):
    print('I received a message!')
    print("raspberry pi received message, do: " + data["message"])


sio.connect(URL)
sio.wait()

