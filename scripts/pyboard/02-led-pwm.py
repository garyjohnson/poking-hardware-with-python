import colorsys
import time
from pyb import Pin,Timer

PIN_R,PIN_G,PIN_B = 'A0','A1','A2'
red,green,blue = (None,None,None)

red = Pin(PIN_R, Pin.OUT_PP)
green = Pin(PIN_G, Pin.OUT_PP)
blue = Pin(PIN_B, Pin.OUT_PP)

for led in [red,green,blue]:
    led.high()

pwm_timer = Timer(2, freq=100)
red_pwm = pwm_timer.channel(2, Timer.PWM, pin=red)
green_pwm = pwm_timer.channel(3, Timer.PWM, pin=green)
blue_pwm = pwm_timer.channel(1, Timer.PWM, pin=blue)

while True:
    for hue in range(0,10000):
        r,g,b = colorsys.hsv_to_rgb(hue/10000.0, 1.0, 1.0)
        red_pwm.pulse_width_percent(r * 100)
        green_pwm.pulse_width_percent(g * 100)
        blue_pwm.pulse_width_percent(b * 100)
        time.sleep(0.001)
