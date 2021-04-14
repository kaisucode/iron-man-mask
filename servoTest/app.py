
import RPi.GPIO as GPIO
import time

def setAngle(angle):
    global servo1
    duty = angle / 18 + 3

    print("duty: " + duty)
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.15)
    servo1.ChangeDutyCycle(0)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo1.start(0) # start duty cycle at zero
print("starting duty cycle at 0")

print("intialized at down position, starting rotation in 1 seconds")

time.sleep(3)
print("test move down")
setAngle(90)


print("moving down in 3 seconds")
time.sleep(3)
print("test move up")
setAngle(0)

