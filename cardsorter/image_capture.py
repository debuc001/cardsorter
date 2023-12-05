import time

from picamera2 import Picamera2, Preview

class image_capture:
 def __init__(self):
  self.picam = Picamera2()
  self.config = self.picam.create_preview_configuration()
  self.picam.configure(self.config)
  #self.picam.start_preview(Preview.QTGL)

 def take_picture(self):
  self.picam.start()
  time.sleep(2)
  self.picam.capture_file("./tmp/card_tmp.jpg")
  self.picam.close()