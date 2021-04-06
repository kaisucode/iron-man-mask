
import socketio
import RPi.GPIO as GPIO
import time

URL = 'http://doranelle.kevinhsu.net:5000/websockets'
sio = socketio.Client()

def setup(): 
    GPIO.setmode(GPIO.BOARD)
    # Set pin 11 as an output, and set servo1 as pin 11 as PWM
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
    servo1.start(0)
    print("GPIO setup complete, pulse set to zero")

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

isOn = False

@sio.on('pi_do')
def pi_do(data):
    print('I received a message!')
    print("raspberry pi received message, do: " + data["message"])
    if isOn: 
        servo1.ChangeDutyCycle(7)
    else: 
        servo1.ChangeDutyCycle(0)
    isOn = !isOn


setup()
sio.connect(URL)
sio.wait()

