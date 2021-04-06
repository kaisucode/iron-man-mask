
import socket


s = socket.socket()
port = 5000
s.connect(('http://localhost:5000/websockets'))
while 1:
    print(s.recv(1024))



#  URL = 'http://localhost:5000/websockets'
#  sio = socketio.Client()

#  @sio.event
#  def connect():
#      print("I'm connected!")

#  #  @sio.event
#  #  def connect_error():
#  #      print("The connection failed!")

#  @sio.event
#  def disconnect():
#      print("I'm disconnected!")

#  @sio.on('pi_do')
#  def pi_do(data):
#      print('I received a message!')
#      print("raspberry pi received message, do: " + data["message"])


#  sio.connect(URL)
#  sio.wait()

