#PIZERO

import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

PIN = 12
G = 11
R = 15

gpio.setup(PIN, gpio.IN, pull_up_down=gpio.PUD_OFF)
gpio.setup(G, gpio.OUT, initial=gpio.HIGH)
gpio.setup(R, gpio.OUT, initial=gpio.HIGH)

previous = False
while True:
    new = gpio.input(PIN)
    gpio.output(G, new)
    gpio.output(R, not new)
    if new != previous:
        print("ON" if new else "OFF")
        previous = new

    time.sleep(0.01)
