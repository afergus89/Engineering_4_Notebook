#GPIO Pins
#Molly and Alex

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

for i in range (1, 11):
    GPIO.output(17,0)
    GPIO.output(18,0)
    sleep(1)
    GPIO.output(17,1)
    GPIO.output(18,1)
    sleep(1)
GPIO.cleanup()
