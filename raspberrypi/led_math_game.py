#!/usr/bin/env python3

import RPi.GPIO as GPIO
import random
import sys
import time

red_led_pin = 11    # RPI Board pin11
green_led_pin = 12  # RPI Board pin11

def setup():
    GPIO.setmode(GPIO.BOARD)               # Numbers GPIOs by physical location
    GPIO.setup(red_led_pin, GPIO.OUT)
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.setup(green_led_pin, GPIO.OUT)
    GPIO.output(green_led_pin, GPIO.LOW)


def loop():
    while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        x = int(input(str(a) + ' + ' + str(b) + " = "))

        if x == a + b:
            pin = green_led_pin
        else:
            pin = red_led_pin

        GPIO.output(pin, GPIO.HIGH)
        time.sleep(2)    
        GPIO.output(pin, GPIO.LOW)


def destroy():
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()