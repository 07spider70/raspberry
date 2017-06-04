#!/usr/bin/python3

import subprocess as sub
import re
import RPi.GPIO as GPIO
from time import sleep

fan_pin = 18    #pin where is fan connected
max_temperature = 20 #our highest comfortable temperature

def setup(pin): #setup pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

def get_temperature():  #return value of temperature
    p = sub.Popen('vcgencmd measure_temp', stdout = sub.PIPE, shell=True)
    output, err = p.communicate()
    temp = re.findall(r'\d+',str(output))
    return temp[0]

def control():
    if int(get_temperature()) >= max_temperature:
        fan_on(fan_pin)
    else:
        fan_off(fan_pin)
    return()

def fan_on(pin):    #fan start
    GPIO.output(pin,True)

def fan_off(pin):   #fan stop
    GPIO.output(pin,False)

def clean_gpio(): #clean GPIO
    GPIO.cleanup()

def main(): #main function
    try:
        setup(fan_pin)
        while True:
            if int(get_temperature()) >= max_temperature:
                fan_on(fan_pin)
            else:
                fan_off(fan_pin)
            sleep(5)
    except:
        clean_gpio()

if __name__ == '__main__':
    main()
