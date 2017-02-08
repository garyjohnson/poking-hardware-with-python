#MICROPYTHON

import colorsys
import time
from pyb import Pin,Timer

R,G,B = 'A0','A1','A2'

red_pin = Pin(R, Pin.OUT_PP)
green_pin = Pin(G, Pin.OUT_PP)
blue_pin = Pin(B, Pin.OUT_PP)

pwm_timer = Timer(2, freq=100)
red = pwm_timer.channel(2, Timer.PWM, pin=red_pin)
green = pwm_timer.channel(3, Timer.PWM, pin=green_pin)
blue = pwm_timer.channel(1, Timer.PWM, pin=blue_pin)

while True:
    for hue in range(0,10000):
        r,g,b = colorsys.hsv_to_rgb(hue/10000.0, 1.0, 1.0)
        red.pulse_width_percent(r * 100)
        green.pulse_width_percent(g * 100)
        blue.pulse_width_percent(b * 100)
        time.sleep(0.001)
