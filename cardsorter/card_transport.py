import time
import RPi.GPIO as GPIO
import logging

from motor_control import *

light_sensor_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_sensor_pin,GPIO.IN)
light_sensor = GPIO.input(light_sensor_pin)
#while True:
# print()

def light_sensor():
 return not GPIO.input(light_sensor_pin)

def card_transport_next():
 #Thats for stopping the motor, if it runs too long (probably an Error occured or there are no more cards)
 end = ((5) + time.time())
 now = time.time()
 
 #give next card and stop dc motor when lightsensor is blocked
 stop_dc_motor = False
 dc_motor_start(40)
 while not stop_dc_motor:
  if not light_sensor():
   stop_dc_motor = True
   dc_motor_stop()
# todo:
  #if end > now:
  # stop_dc_motor = True
  # logging.info('No more cards to run') 
