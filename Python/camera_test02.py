from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False, window=(10,20,900,1200)) #y,x,h,w
sleep(2)

for effect in myCamera.IMAGE_EFFECTS:
    print(effect)
    myCamera.image_effect = effect
    myCamera.annotate_text_size = 150
    myCamera.annotate_text = "Check out our cool filters!"
    sleep(5)
    filename = "myPic_%s.jpg" % effect
    if effect == "cartoon":
        myCamera.capture(filename)
    if effect == "negative":
        myCamera.capture(filename)
    if effect == "watercolor":
        myCamera.capture(filename)
    if effect == "sketch":
        myCamera.capture(filename)
    if effect == "emboss":
        myCamera.capture(filename)
myCamera.stop_preview()
