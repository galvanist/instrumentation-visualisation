import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

r = GPIO.PWM(7,50)
g = GPIO.PWM(11,50)
b = GPIO.PWM(15,50)
r.start(0)
g.start(0)
b.start(0)

for dc in range(0, 101, 5):
    r.ChangeDutyCycle(dc)
    g.ChangeDutyCycle(dc)
    b.ChangeDutyCycle(dc)
    time.sleep(0.5)
    print dc
for dc in range(100, 0, -5):
    r.ChangeDutyCycle(dc)
    g.ChangeDutyCycle(dc)
    b.ChangeDutyCycle(dc)
    time.sleep(0.5)
    print dc

r.ChangeDutyCycle(0)
g.ChangeDutyCycle(0)
b.ChangeDutyCycle(0)

GPIO.cleanup()
