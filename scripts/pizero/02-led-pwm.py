import colorsys
import time
import RPi.GPIO as gpio

PIN_R,PIN_G,PIN_B = 15,11,13
red,green,blue = (None,None,None)

gpio.setmode(gpio.BOARD)

for pin in [PIN_R,PIN_G,PIN_B]:
    gpio.setup(pin, gpio.OUT, initial=gpio.HIGH)

red = gpio.PWM(PIN_R,100)
green = gpio.PWM(PIN_G,100)
blue = gpio.PWM(PIN_B,100)

for led in [red,green,blue]:
    led.start(0)

while True:
    for hue in range(0,10000):
        r,g,b = colorsys.hsv_to_rgb(hue/10000.0, 1.0, 1.0)
        red.ChangeDutyCycle(r * 100)
        green.ChangeDutyCycle(g * 100)
        blue.ChangeDutyCycle(b * 100)
        time.sleep(0.001)
