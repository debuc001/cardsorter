import pandas as pd
import requests
import json
import numpy as np
import time
import logging

#import RPi.GPIO as GPIO


from wanted_cards_dataframe import *
from image_manipulation import *
from image_recognition import *
#from motor_control import *

scryfall_base_api_url = "https://api.scryfall.com/"
scryfall_cardname_object = "cards/named?exact=!"
image_input = "../tests/testcard.jpg"

wanted_cards = WantedCards()
wanted_cards.print_dataframe_wanted_cards()

#crop_image(image_input, get_image_width(image_input) - 150, 100)
#cropped_image = "../tests/testcard_cropped.jpg"
#text_recognition(cropped_image)

#init_dc_motor()
#init_servo_motor()
#set_servo_motor_middle()


#while True:
# dc_motor_give_card()
# set_servo_motor_left()
# time.sleep(0.2)
# set_servo_motor_middle()

#set_servo_motor_left()
#time.sleep(5)
#set_servo_motor_right()
#time.sleep(5)
#set_servo_motor_stop()

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.IN)
#while True:
# print(GPIO.input(17))



logging.info('This message is just informative')
logging.debug('My missions is to provide information about debugging.')
logging.critical("A Critical Logging Message")