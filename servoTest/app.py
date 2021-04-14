
import RPi.GPIO as GPIO
import time

def setAngle(angle, timeInterval):
    global servo1
    duty = angle / 18 + 3

    print("duty: " + str(duty))
    servo1.ChangeDutyCycle(duty)
    time.sleep(timeInterval) # save value
    #  time.sleep(0.15) # save value
    servo1.ChangeDutyCycle(0)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo1.start(0) # start duty cycle at zero
print("starting duty cycle at 0")

print("intialized at down position, starting rotation in 1 seconds")

time.sleep(3)
print("test move down")
setAngle(90, 0.08)


print("moving down in 3 seconds")
time.sleep(3)
print("test move up")
setAngle(0, 0.24)

