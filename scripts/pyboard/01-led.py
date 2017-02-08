import time
from pyb import Pin

PIN_R,PIN_G,PIN_B = 'A0','A1','A2'
red,green,blue = (None,None,None)

def light_pin(lit_pin):
    for led in [red,green,blue]:
        led.value(led.name() != lit_pin)

red = Pin(PIN_R, Pin.OUT_PP)
green = Pin(PIN_G, Pin.OUT_PP)
blue = Pin(PIN_B, Pin.OUT_PP)

for led in [red,green,blue]:
    led.high()

while True:
    for pin in [PIN_R,PIN_G,PIN_B]:
        light_pin(pin)
        time.sleep(1)
