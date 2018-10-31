#Print accelerometer and magnetometer X,Y, Z axis values every .5 second.
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
padding = 2
shape_width = 20
top = padding
bottom = height-padding
draw = ImageDraw.Draw(image)
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Load default font.
font = ImageFont.load_default()

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
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
    # Wait half a second and repeat.
    time.sleep(0.5)

    draw.text((x, top),    'Accel data',  font=font, fill=255)
    draw.text((x, top+20),    myStrx, font=font, fill=255)
    draw.text((x, top+30),    myStry,  font=font, fill=255)
    draw.text((x, top+40),    myStrz,  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()

