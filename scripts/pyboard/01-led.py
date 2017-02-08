#MICROPYTHON

import time
from pyb import Pin

R,G,B = 'A0','A1','A2'

def light_pin(lit_pin):
    for led in [red,green,blue]:
        led.value(led.name() != lit_pin)


red = Pin(R, Pin.OUT_PP)
green = Pin(G, Pin.OUT_PP)
blue = Pin(B, Pin.OUT_PP)

for led in [red,green,blue]:
    led.high()

while True:
    for pin in [R,G,B]:
        light_pin(pin)
        time.sleep(1)
