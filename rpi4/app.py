
import socketio
import RPi.GPIO as GPIO
import time

URL = 'http://doranelle.kevinhsu.net:5000/websockets'
sio = socketio.Client()

isOn = False

GPIO.setmode(GPIO.BOARD)
# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # Note 11 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(12, 50) # Note 12 is pin, 50 = 50Hz pulse
servo1.start(0)
servo2.start(0)
print("GPIO setup complete, pulse set to zero")

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

def setAngle(angle):
    global gpio
    global servo1
    duty = angle / 18 + 3
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11, False)
    servo1.ChangeDutyCycle(duty)

@sio.on('pi_do')
def pi_do(data):
    #  global isOn
    global servo1
    global servo2
    print('I received a message!')
    print("raspberry pi received message, do: " + data["message"])
    if data["message"] == "open mask": 
        setAngle(180)
        #  servo1.ChangeDutyCycle(7)
        #  servo2.ChangeDutyCycle(7)
        #  time.sleep(3)
        #  servo1.ChangeDutyCycle(0)
        #  servo2.ChangeDutyCycle(0)
    elif data["message"] == "close mask": 
        setAngle(0)
        #  servo1.ChangeDutyCycle(-7)
        #  servo2.ChangeDutyCycle(-7)
        #  time.sleep(3)
        #  servo1.ChangeDutyCycle(0)
        #  servo2.ChangeDutyCycle(0)
    #  isOn = not isOn


#  setup()
setAngle(0)
sio.connect(URL)
sio.wait()

