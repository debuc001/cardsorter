import logging

logging.basicConfig(level=logging.INFO)

import card_transport as ct
import image_capture as ic
import image_recognition as ir
import wanted_cards_dataframe as wcdf

wanted_cards = wcdf.WantedCards()
camera = ic.image_capture()
img_recog = ir.ImageRecognition()

camera.focus_maual()


ct.card_transport_next()
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
if is_card_wanted == False:
  logging.info('Card is not wanted or not recognized')
  logging.info('Card goes right')
 