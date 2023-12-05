import time

from picamera2 import Picamera2, Preview

def image_capture():
 picam = Picamera2()
 config = picam.create_preview_configuration()
 picam.configure(config)
 #picam.start_preview(Preview.QTGL)

 def take_picture():
  picam.start()
  time.sleep(2)
  picam.capture_file("./tmp/card_tmp.jpg")
  picam.close()