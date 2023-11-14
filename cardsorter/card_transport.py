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
 #give next card and stop dc motor when lightsensor is blocked
 dc_motor_start(50)
 while GPIO.input(light_sensor_pin):
  dc_motor_stop()
 #decide if card is wanted or not
 #WIP: ONLY FOR TEST:
 card_is_wanted = True
 if card_is_wanted:
  servo_motor_set_angle("left")
 else:
  servo_motor_set_angle("right")
 sleep(2)
 servo_motor_set_angle("mid")

