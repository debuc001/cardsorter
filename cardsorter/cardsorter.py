import logging

logging.basicConfig(level=logging.INFO)

import card_transport as card_transport
import image_capture as ic
import image_recognition as ir
import wanted_cards_dataframe as wcdf
import motor_control as motor_control

wanted_cards = wcdf.WantedCards()
camera = ic.image_capture()
img_recog = ir.ImageRecognition()

camera.focus_maual()


card_transport.card_transport_next()
camera.take_picture()
#compare cards
card_captured = img_recog.recognize()
is_card_wanted = False
for ind in wanted_cards.deckstats_card_dataframe.index:
 cardname = wanted_cards.deckstats_card_dataframe.iat[ind,1]
 if card_captured == cardname:
  is_card_wanted = True
  logging.info('Card is wanted: ' + cardname)
  logging.info('Card goes left')
  card_transport.left_or_right("left")
if is_card_wanted == False:
  logging.info('Card is not wanted or not recognized')
  logging.info('Card goes right')
  card_transport.left_or_right("right")
 