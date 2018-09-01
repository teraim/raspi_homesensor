#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
for x in range(10000):
  GPIO.output(21,1)
  sleep(2)
  GPIO.output(21,0)
  sleep(2)
GPIO.cleanup()
