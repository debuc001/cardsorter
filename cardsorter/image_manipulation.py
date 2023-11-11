from PIL import Image

#WIP
def get_image_width(image):
 img = open_image(image) 
 w, h = img.size
 return w

def get_image_height(image):
 img = open_image(image) 
 w, h = img.size
 return h

def crop_image(image, width, height):
 img = open_image(image) 
 
 left = 10
 top = 10
 right = width
 bottom = height
  
 img_res = img.crop((left, top, right, bottom)) 
 
 img_res = img_res.save("../tests/testcard_cropped.jpg") 

def open_image(image):
 return Image.open(image, mode = 'r')