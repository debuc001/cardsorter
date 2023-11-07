from PIL import Image

#WIP
def get_image_size(image):
 img = open_image(image) 
 w, h = img.size
 return w, h
 print('width: ', w)
 print('height:', h)

def crop_image(image):
 img = open_image(image) 
 
 left = 0
 top = 0
 right = 510
 bottom = 292
  
 img_res = img.crop((left, top, right, bottom)) 
 
 img_res = img_res.save("../tests/testcard_cropped.jpg") 

def open_image(image):
 return Image.open(image, mode = 'r')