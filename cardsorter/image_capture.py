import time

from picamera2 import Picamera2, Preview
from libcamera import controls

class image_capture:
 def __init__(self):
  self.picam = Picamera2()
  #self.config = self.picam.create_preview_configuration()
  #self.picam.configure(self.config)
  #self.picam.start_preview(Preview.QTGL)

 def trigger_autofocus(self):
  self.picam.start(show_preview=True)
  #success = self.picam.autofocus_cycle()
  while self.picam.autofocus_cycle():
   time.sleep(0.1)

 def take_picture(self):
  self.picam.start()
  time.sleep(2)
  self.picam.capture_file("./tmp/card_tmp.jpg")
  self.picam.close()