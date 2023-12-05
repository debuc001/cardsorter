from card_transport import *
from image_capture import *
from image_recognition import *
from motor_control import *
from wanted_cards_dataframe import *

wanted_cards = WantedCards()
wanted_cards.print_dataframe_wanted_cards()
camera = image_capture()


while True:
 card_transport_next()
 camera.take_picture()
 #compare cards

