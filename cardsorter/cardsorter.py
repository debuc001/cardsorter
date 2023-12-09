import logging

logging.basicConfig(level=logging.DEBUG)

#from card_transport import *
#from image_capture import *
from image_recognition import *
#from motor_control import *
from wanted_cards_dataframe import *

wanted_cards = WantedCards()
#camera = image_capture()
img_recog = ImageRecognition()


#card_transport_next()
#camera.take_picture()
#compare cards
card_captured = img_recog.recognize()
is_card_wanted = False
for ind in wanted_cards.deckstats_card_dataframe.index:
 cardname = wanted_cards.deckstats_card_dataframe.iat[ind,1]
 if card_captured == cardname:
  is_card_wanted = True
  logging.info('Card is wanted: ' + cardname)
  logging.info('Card goes left')
if is_card_wanted == False:
  logging.info('Card is not wanted or not recognized')
  logging.info('Card goes right')
 