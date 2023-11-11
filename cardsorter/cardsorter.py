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

servo_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm=GPIO.PWM(servo_pin, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)

count = 0
numLoops = 2

while count < numLoops:
    print("set to 0-deg")
    setAngle(20)
    time.sleep(1)

        
    print("set to 90-deg")
    setAngle(90)
    time.sleep(1)

    print("set to 135-deg")
    setAngle(160)
    time.sleep(1)
    
    count=count+1

pwm.stop()
GPIO.cleanup()