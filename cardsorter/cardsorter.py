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

#crop_image(image_input, get_image_width(image_input) - 150, 100)
#cropped_image = "../tests/testcard_cropped.jpg"
#text_recognition(cropped_image)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.IN)
#while True:
# print(GPIO.input(17))