import pandas as pd

deckstats_card_dataframe = pd.DataFrame( columns = ['QUANTITY','CARDNAME'])

#create dataframe from file resources/deckstats_cardlist.txt
def get_deckstats_card_dataframe():
 with open("resources/deckstats_cardlist.txt") as file:
  for item in file:
   #seperate quantity and cardnames, remove newline
   line_from_deckstats_cardlist = item.split(sep=" ",maxsplit=1)
   line_from_deckstats_cardlist = [r.strip() for r in line_from_deckstats_cardlist]
   #add each modified line to dataframe
   deckstats_card_dataframe.loc[len(deckstats_card_dataframe)] = line_from_deckstats_cardlist
 return deckstats_card_dataframe

deckstats_card_dataframe = get_deckstats_card_dataframe()
print(deckstats_card_dataframe)

