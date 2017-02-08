#MICROPYTHON

import time
import pyb
from pyb import Pin

PIN = 'A3'
G = 'A1'
R = 'A2'

switch = Pin(PIN, Pin.IN, Pin.PULL_NONE)
green_led = Pin(G, Pin.OUT_PP)
red_led = Pin(R, Pin.OUT_PP)
green_led.high()
red_led.high()

previous = False
while True:
    new = bool(switch.value())
    green_led.value(new)
    red_led.value(not new)
    if new != previous:
        print("ON" if new else "OFF")
        previous = new

    time.sleep(0.01)
