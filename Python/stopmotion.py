#stopmotion

from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
mycamera = PiCamera()

#mycamera.start_preview(fullscreen=False, window=(10,20,900,1200))
frame = 1
while True:
    try:
        button.wait_for_press()
        print ("button pressed")
        mycamera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        #mycamera.stop_preview()
        break 
