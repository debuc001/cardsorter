import os
import sys
 
# setting path
sys.path.append('..')

from wanted_cards_dataframe import *

# setting path
os.chdir('..')

#Print out the wanted cards
wanted_cards = WantedCards()
wanted_cards.print_dataframe_wanted_cards()