#from card_transport import *
from image_capture import *
from image_recognition import *
#from motor_control import *
from wanted_cards_dataframe import *

wanted_cards = WantedCards()
camera = image_capture()
img_recog = ImageRecognition()


#card_transport_next()
camera.take_picture()
#compare cards
card_captured = img_recog.recognize()
is_card_wanted = False
for ind in wanted_cards.deckstats_card_dataframe.index:
 cardname = wanted_cards.deckstats_card_dataframe.iat[ind,1]
 if card_captured == cardname:
  is_card_wanted = True
