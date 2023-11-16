import time
import RPi.GPIO as GPIO

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
 #give next card and stop dc motor when lightsensor is blocked
 stop_dc_motor = True
 dc_motor_start(40)
 while stop_dc_motor:
  if not light_sensor():
   stop_dc_motor = False
   dc_motor_stop()

 #decide if card is wanted or not
 #WIP: ONLY FOR TEST:
 time.sleep(1)
 card_is_wanted = True
 if card_is_wanted is True:
   servo_motor_set_angle("left")
 else:
   servo_motor_set_angle("right")
 time.sleep(2)
 servo_motor_set_angle("mid")

