#PIZERO

import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

R,G,B = 15,11,13

def light_pin(lit_pin):
    for pin in [R,G,B]:
        gpio.output(pin, pin != lit_pin)


for pin in [R,G,B]:
    gpio.setup(pin, gpio.OUT, initial=gpio.HIGH)

while True:
    for pin in [R,G,B]:
        light_pin(pin)
        time.sleep(1)
