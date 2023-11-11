import pandas as pd
import requests
import json
import numpy as np
import time
from gpiozero import AngularServo


from dataframe_functions import *
from image_manipulation import *
from image_recognition import *
from motor_control import *

deckstats_card_dataframe = pd.DataFrame( columns = ['QUANTITY','CARDNAME_EN'])
scryfall_base_api_url = "https://api.scryfall.com/"
scryfall_cardname_object = "cards/named?exact=!"
image_input = "../tests/testcard.jpg"

#Create dataframe 
deckstats_card_dataframe = get_deckstats_card_dataframe(deckstats_card_dataframe)
deckstats_card_dataframe = preprocessing_dataframe(deckstats_card_dataframe)

#print(deckstats_card_dataframe)

#crop_image(image_input, get_image_width(image_input) - 150, 100)
#cropped_image = "../tests/testcard_cropped.jpg"
#text_recognition(cropped_image)

#init_dc_motor()
#start_dc_motor(25)
#time.sleep(0.5)
#stop_dc_motor()

servo = AngularServo(21, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    servo.angle = 90
    time.sleep(2)
    servo.angle = 0
    time.sleep(2)
    servo.angle = -90
    time.sleep(2)