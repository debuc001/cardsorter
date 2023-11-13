import time
import RPi.GPIO as GPIO

from motor_control import *

light_sensor_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_sensor_pin,GPIO.IN)
light_sensor = GPIO.input(light_sensor_pin)
#while True:
# print()

def card_transport_next():
 dc_motor_start(50)
 print(GPIO.input(light_sensor_pin))
 while GPIO.input(light_sensor_pin):
  print("TEST: light sensor true : ")
  print(GPIO.input(light_sensor_pin))
 dc_motor_stop()