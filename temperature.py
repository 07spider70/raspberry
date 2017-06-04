

import subprocess
import re
import RPi.GPIO as GPIO

#SETUP
pin = 18
teplota_max = 40


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

#vykona prikaz cmd
p = subprocess.Popen('vcgencmd measure_temp', stdout = subprocess.PIPE, shell=True)
output, err = p.communicate()
#vrati string

#najde a ulozi teplotu do temp (cele cislo)
temp = re.findall(r'\d+',str(output))

#ak je vysoka teplota pusti chladenie
if int(temp[0]) >= teplota_max:
	print('High ', temp[0])
	GPIO.output(pin,True)

else:
	print('Normal') 
	GPIO.cleanup()
