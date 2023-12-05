from mtgscan.text import MagicRecognition
from mtgscan.ocr.azure import Azure
import os

def image_recognition():
 os.environ['AZURE_VISION_ENDPOINT'] = 'https://mtgscan-cvr.cognitiveservices.azure.com/'
 os.environ['AZURE_VISION_KEY'] = '1dee066d4686498596110672904ec81a'
 
 azure = Azure()
 rec = MagicRecognition(file_all_cards="all_cards.txt", file_keywords="Keywords.json")

 def compare(image):
  box_texts = azure.image_to_box_texts(image)
  deck = rec.box_texts_to_deck(box_texts)
  for c, k in deck:
   print(c, k)