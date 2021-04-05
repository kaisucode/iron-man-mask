
import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('send_message')
def send_message(sid, res): 
    print("received and sending: " + res.data)
    sio.emit('pi_do', { 'message': res.data })

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

