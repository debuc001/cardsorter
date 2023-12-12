import time
from picamera2 import Picamera2, Preview
from libcamera import controls

class image_capture:
 def __init__(self):
  self.picam = Picamera2()
  config = self.picam.create_preview_configuration()
  self.picam.configure(config)

#autofocus not working
# def trigger_autofocus(self):
  #success = self.picam.autofocus_cycle()

 def focus_maual(self):
  self.picam.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 4.15})
  self.picam.start()
  time.sleep(2)

 def take_picture(self):
  self.picam.start()
  time.sleep(2)
  self.picam.capture_file("./tmp/card_tmp.jpg")
  
 def close_camera(self):
  self.picam.close()

