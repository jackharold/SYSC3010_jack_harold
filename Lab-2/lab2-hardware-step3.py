from sense_hat import SenseHat
from random import randint
from time import sleep
from math import floor

# Lab 2 Step 3
# Created by Jack Harold 09/25/20
# Base code from http://projects.raspberrypi.org/en/projects/sense-hat-ransom-sparkles/

sense = SenseHat();

x = randint(0, 7)
y = randint(0, 7)
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
temp = floor(sense.get_temperature())
pressure = floor(sense.get_pressure())
humidity = floor(sense.get_humidity())

print("Currently " + str(temp) + " decrees C")
print("Currently " + str(pressure) + "mbar")
print("Currently " + str(humidity) + "% humidity")

def update_pixel():
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    return

sense.clear()
while True:
    sleep(2)
    update_pixel()