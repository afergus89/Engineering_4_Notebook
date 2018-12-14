import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time

GPIO.setmode(GPIO.BCM)
sensor = MotionSensor(17)
GPIO.setup(19, GPIO.OUT)

print("about to start")

while True:
    print("waiting for motion")
    sensor.wait_for_motion()
    print ("Caught YOU!")
    GPIO.output(19, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(19, GPIO.LOW)
    sensor.wait_for_no_motion()
    print ("Clear")
    time.sleep(1)
