from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False, window=(10,20,900,1200)) #y,x,h,w

myCamera.start_recording('video01.h264')
sleep (10)
myCamera.stop_recording()
