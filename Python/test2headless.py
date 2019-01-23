#Print an acceleration graph on an OLED screen.
#Author: Tony DiCola
#Molly and Alex
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
image2 = Image.new('1', (50,12))
padding = 2
shape_width = 20
top = padding
bottom = height-padding
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
x1 = 10
x2 = 10
i = 0
yarr = [50]
# Load default font.
font = ImageFont.load_default()

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    myStrx = 'x = ' + str(abs(accel_x/100))
    myStry = 'y = ' + str(accel_y/100)
    myStrz = 'z = ' + str(accel_z/100)
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    accel_y = abs(accel_y)
    x1 = x1+10
    y1 = (bottom - 10) - accel_y
    if y1 < 0:
        y1 = 0
    yarr.append(y1)
    if len(yarr) < 15:
        yarr.pop(0)
    

    draw.line((x, bottom-10,  x+width, bottom-10), fill=255)
    #draw.line((x+10, bottom-10, x+10, top), fill=255)
    draw.rectangle((0,0,width,bottom-15), outline=0, fill=0)
    draw.rectangle((x+10, bottom-30, accel_y/10, bottom-40), fill=255)
    draw.text((x+40, bottom-9), 'a (m/s2)',  font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
