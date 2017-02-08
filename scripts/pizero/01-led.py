import time
import RPi.GPIO as gpio

PIN_R,PIN_G,PIN_B = 15,11,13
pins = (PIN_R,PIN_G,PIN_B)

def light_pin(lit_pin):
    for pin in pins:
        gpio.output(pin, pin != lit_pin)

gpio.setmode(gpio.BOARD)

for pin in pins:
    gpio.setup(pin, gpio.OUT, initial=gpio.HIGH)

while True:
    for pin in pins:
        light_pin(pin)
        time.sleep(1)
