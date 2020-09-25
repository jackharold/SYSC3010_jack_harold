from sense_hat import SenseHat
import time

# Letter switching program
# Created by Jack Harold 09/24/20
# Using techniques from the Rock Paper Pi and the starting example

sense = SenseHat()

R = (255, 0, 0)
Y = (255, 255, 0)
G = (0, 255, 0)
B = (0, 0, 255)
X = (0, 0, 0)

capital_J = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, R, R, R, X, X,
    X, X, X, X, R, X, X, X,
    X, X, X, X, R, X, X, X,
    X, X, R, X, R, X, X, X,
    X, X, R, R, R, X, X, X,
    X, X, X, X, X, X, X, X
]

capital_H = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, B, X, B, X, X,
    X, X, X, B, X, B, X, X,
    X, X, X, B, B, B, X, X,
    X, X, X, B, X, B, X, X,
    X, X, X, B, X, B, X, X,
    X, X, X, X, X, X, X, X
]

current_image = capital_J
sense.clear()
sense.set_pixels(capital_J)

####
# Main Loop
####

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            #this is a hold or keyup; move on
            continue
        if current_image == capital_J:
            current_image = capital_H
            sense.set_pixels(current_image)
        elif current_image == capital_H:
            current_image = capital_J
            sense.set_pixels(current_image)