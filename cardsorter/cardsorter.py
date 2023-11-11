import pandas as pd
import requests
import json
import numpy as np
import time
import RPi.GPIO as GPIO



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


servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  while True:
    p.ChangeDutyCycle(5)
    print("-90")
    time.sleep(2)
    p.ChangeDutyCycle(7.5)
    print("0")
    time.sleep(2)
    p.ChangeDutyCycle(10)
    print("+90")
    time.sleep(2)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()