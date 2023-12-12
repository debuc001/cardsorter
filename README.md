# cardsorter
A bot to sort magic cards.

This Project is inspired by: https://github.com/kbelenky/open_sorts
Thanks to kbelenky.

--PART LIST--
Here is a list of the main parts for this project:
  - Raspberry Pi 3b+
  - DFRobot motor driver hat, see https://wiki.dfrobot.com/DC_Motor_Driver_HAT_SKU_DFR0592
    - I think only the pins 39(Ground), 3(SDA1) and 5(SCL1) are used by this motor driver. The remaining pins can be used freely.
  - 5MP camera for Raspberry Pi
  - lightsensor
  - Adafruit Micro Servo: https://www.adafruit.com/product/4326 , https://www.towerpro.com.tw/product/sg92r-7/ 

--INSTRUCTIONS--
For the servo we need pigpio to run. You can enable and start it with:
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

Checkout the docu for picamera2: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
