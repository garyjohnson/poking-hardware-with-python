#PIZERO

import colorsys
import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

R,G,B = 15,11,13

for pin in [R,G,B]:
    gpio.setup(pin, gpio.OUT, initial=gpio.HIGH)

red = gpio.PWM(R,100)
green = gpio.PWM(G,100)
blue = gpio.PWM(B,100)

for led in [red,green,blue]:
    led.start(0)

while True:
    for hue in range(0,10000):
        r,g,b = colorsys.hsv_to_rgb(hue/10000.0, 1.0, 1.0)
        red.ChangeDutyCycle(r * 100)
        green.ChangeDutyCycle(g * 100)
        blue.ChangeDutyCycle(b * 100)
        time.sleep(0.001)
