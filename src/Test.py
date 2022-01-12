import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

prev_inpt = 1
while True:
    inpt = GPIO.input(5)
    if ((not prev_inpt) and inpt):
        print("Button pressed")
    prev_inpt = inpt
    time.sleep(0.05)