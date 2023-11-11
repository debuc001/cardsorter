#import pytesseract
from PIL import Image

def text_recognition(image):
 # Perform OCR using PyTesseract
 #text = pytesseract.image_to_string(Image.open(image), timeout=2, lang="eng")

 # Print the extracted text
 print(text)