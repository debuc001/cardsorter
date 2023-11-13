import numpy
import pandas
import requests
import logging

class WantedCards:
 def __init__(self):
  self.deckstats_card_dataframe = pandas.DataFrame( columns = ['QUANTITY','CARDNAME_EN'])

 #Fill dataframe from file resources/deckstats_cardlist.txt
  with open("./deckstats_cardlist.txt") as file:
   for item in file:
    #Seperate quantity and cardnames, remove newline
    line_from_deckstats_cardlist = item.split(sep=" ",maxsplit=1)
    line_from_deckstats_cardlist = [r.strip() for r in line_from_deckstats_cardlist]
    #Add each modified line to dataframe
    self.deckstats_card_dataframe.loc[len(self.deckstats_card_dataframe)] = line_from_deckstats_cardlist
  logging.info('Dataframe for wanted cards is filled')

  #Remove everything after // -> only one name of double sided card is left in dataframe
  for ind in self.deckstats_card_dataframe.index:
   cardname = self.deckstats_card_dataframe.iat[ind,1]
   head, sep, tail = cardname.partition('//')
   self.deckstats_card_dataframe.iat[ind,1] = head
  #Remove everything after # -> only the name of the commander is left
  for ind in self.deckstats_card_dataframe.index:
   cardname = self.deckstats_card_dataframe.iat[ind,1]  
   head, sep, tail = cardname.partition('#')
   self.deckstats_card_dataframe.iat[ind,1] = head
  logging.info('Dataframe for wanted cards is cleaned')

 def print_dataframe_wanted_cards(self):
  print(self.deckstats_card_dataframe)

  
#
#Add support for german cards.
#This is not supported yet.
#
def add_row_for_german_cards(dataframe):
 dataframe['CARDNAME_DE'] = numpy.nan

def fill_dataframe_with_cardnames_de(dataframe, scryfall_base_api_url, scryfall_cardname_object):
 for ind in dataframe.index:
  #Get the english cardnames from dataframe
  cardname = dataframe.iat[ind,1]
  scryfall_request_cardname_api_url = scryfall_base_api_url + scryfall_cardname_object + "\"" + cardname + "\""
  response_english_card = requests.get(scryfall_request_cardname_api_url)
  #Report if request fails
  if response_english_card.status_code != 200:
   print(response_english_card.status_code)

  #Build request for german cardname  
  scryfall_card_json = response_english_card.json()
  scryfall_set_cn_api_url = scryfall_base_api_url + "cards/" + scryfall_card_json['set'] + "/" +  scryfall_card_json['collector_number'] + "/de"
  response_german_card = requests.get(scryfall_set_cn_api_url)
  #Request the german card name. If no german equivalent is found, ignore the request.
  try:
   dataframe.iat[ind,2] = response_german_card.json()['printed_name']
  except KeyError:
   print("It seems that the card \"" + scryfall_card_json['name'] + "\" has no german equivalent")
   print(scryfall_set_cn_api_url)
 return dataframe