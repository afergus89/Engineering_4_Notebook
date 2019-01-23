#Parent-detector

import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import time

GPIO.setmode(GPIO.BCM)
sensor = MotionSensor(4)
myCamera = PiCamera()

#myCamera.start_preview(fullscreen=False, window=(10,20,900,1200)) #y,x,h,w

while True:
    print("waiting for motion")
    sensor.wait_for_motion()
    print ("Caught YOU!")
    myCamera.start_recording('intruder.h264')
    myCamera.wait_recording(5)
    myCamera.stop_recording()
    sensor.wait_for_no_motion()
    print ("Clear")
    time.sleep(1)


##print ("recording")
##myCamera.start_recording('test2.h264')
##myCamera.wait_recording(5)
##myCamera.stop_recording()
##myCamera.stop_preview()
##print ("done")
