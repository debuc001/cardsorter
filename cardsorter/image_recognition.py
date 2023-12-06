from mtgscan.text import MagicRecognition
from mtgscan.ocr.azure import Azure
import os

class ImageRecognition:
 def __init__(self):
  os.environ['AZURE_VISION_ENDPOINT'] = 'https://mtgscan-cvr.cognitiveservices.azure.com/'
  os.environ['AZURE_VISION_KEY'] = '1dee066d4686498596110672904ec81a'
 
  self.azure = Azure()
  self.rec = MagicRecognition(file_all_cards="all_cards.txt", file_keywords="Keywords.json")

 def recognize(self):
  box_texts = self.azure.image_to_box_texts("./tmp/card_tmp.jpg")
  deck = self.rec.box_texts_to_deck(box_texts)
  for c, k in deck:
   print(c, k)
  return c