import pandas as pd
import requests
import json
import numpy as np
import time



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

init_dc_motor()
init_servo_motor()
set_servo_motor_middle()

while True:
 dc_motor_give_card()
 set_servo_motor_left()
 time.sleep(0.2)
 set_servo_motor_middle()


set_servo_motor_stop()