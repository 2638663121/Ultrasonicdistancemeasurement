import os
import sys
#import os
import RPi.GPIO as GPIO
import time
from time import sleep
print "program started"
#A='38'
B=40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(7,GPIO.IN)
GPIO.setup(B,GPIO.IN)
GPIO.setup(38,GPIO.IN)


  # os.system('sudo halt')
# try:
#   os._exit()
# try:
#  sys.exit(0)
# except:
#  print 'die'
# finally:
#  print 'cleanup'


while(1):

 if(GPIO.input(38) == 1):
  time.sleep(1)
  #print("sexy")
  os.system('sudo halt')

 if (GPIO.input(B) == 0):
  #write something
  time.sleep(0)
 else:
  GPIO.output(12,True)
  time.sleep(0.00001)
  GPIO.output(12,False)

  while GPIO.input(7) == 0:
    pass
  pulse_start = time.time()

  while GPIO.input(7) == 1:
     pass
  pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance,2)
  sleep(0.5)
  print("distance is"+format(distance)+"cm")

  
