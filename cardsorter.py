import pandas as pd
import requests
import json
import numpy as np

deckstats_card_dataframe = pd.DataFrame( columns = ['QUANTITY','CARDNAME_EN'])
scryfall_base_api_url = "https://api.scryfall.com/"
scryfall_cardname_object = "cards/named?exact=!"

#Create dataframe from file resources/deckstats_cardlist.txt
def get_deckstats_card_dataframe():
 with open("resources/deckstats_cardlist.txt") as file:
  for item in file:
   #Seperate quantity and cardnames, remove newline
   line_from_deckstats_cardlist = item.split(sep=" ",maxsplit=1)
   line_from_deckstats_cardlist = [r.strip() for r in line_from_deckstats_cardlist]
   #Add each modified line to dataframe
   deckstats_card_dataframe.loc[len(deckstats_card_dataframe)] = line_from_deckstats_cardlist
 return deckstats_card_dataframe

def preprocessing_dataframe(dataframe):
 for ind in dataframe.index:
  cardname = dataframe.iat[ind,1]
  head, sep, tail = cardname.partition('//')
  dataframe.iat[ind,1] = head
 for ind in dataframe.index:
  cardname = dataframe.iat[ind,1]  
  head, sep, tail = cardname.partition('#')
  dataframe.iat[ind,1] = head
 return dataframe

def add_row_for_german_cards(dataframe):
 dataframe['CARDNAME_DE'] = np.nan

def fill_dataframe_with_cardnames_de():
 for ind in deckstats_card_dataframe.index:
  #Get the english cardnames from dataframe
  cardname = deckstats_card_dataframe.iat[ind,1]
  scryfall_request_cardname_api_url = scryfall_base_api_url + scryfall_cardname_object + "\"" + cardname + "\""
  response_english_card = requests.get(scryfall_request_cardname_api_url)
  #Report if request fails
  if response_english_card.status_code != 200:
   print(response_english_card.status_code)

  #Build request for german cardname  
  scryfall_cardname = response_english_card.json()
  scryfall_set_cn_api_url = scryfall_base_api_url + "cards/" + scryfall_cardname['set'] + "/" +  scryfall_cardname['collector_number'] + "/de"
  response_german_card = requests.get(scryfall_set_cn_api_url)
  #Request the german card name. If no german equivalent is found, ignore the request.
  try:
   deckstats_card_dataframe.iat[ind,2] = response_german_card.json()['printed_name']
  except KeyError:
   print("It seems that the card \"" + scryfall_cardname['name'] + "\" has no german equivalent")
 return deckstats_card_dataframe




deckstats_card_dataframe = get_deckstats_card_dataframe()
#add_row_for_german_cards(deckstats_card_dataframe)
#deckstats_card_dataframe = fill_dataframe_with_cardnames_de()
deckstats_card_dataframe = preprocessing_dataframe(deckstats_card_dataframe)
print(deckstats_card_dataframe)
