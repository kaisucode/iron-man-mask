
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo1.start(0) # start duty cycle at zero

print("intialized at down position")



def setAngle(angle):
    global servo1
    duty = angle / 18 + 3

    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    servo1.ChangeDutyCycle(0)


print("test move up")
setAngle(90)

print("test move down")
setAngle(0)

