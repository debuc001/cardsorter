import time
import RPi.GPIO as GPIO
import logging
import pigpio
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

from DFRobot_RaspberryPi_DC_Motor import THIS_BOARD_TYPE, DFRobot_DC_Motor_IIC as Board

#select bus 1, set address to 0x10
board = Board(1, 0x10)

#Init servo motor
servo = pigpio.pi()
servo_pin = 21


def print_board_status():
 if board.last_operate_status == board.STA_OK:
  print("board status: everything ok")
 elif board.last_operate_status == board.STA_ERR:
  print("board status: unexpected error")
 elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
  print("board status: device not detected")
 elif board.last_operate_status == board.STA_ERR_PARAMETER:
  print("board status: parameter error, last operate no effective")
 elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
  print("board status: unsupport board framware version")

def dc_motor_init():
 #select motor driver
 try:
    with open('/proc/device-tree/model', 'r') as f:
        model = f.read()
 except:
    pass

 #check status
 time.sleep(2)
 if board.begin() == board.STA_OK:
  print("board begin success")
 else:
  print_board_status()
  print("board begin failed")

 # Set selected DC motor encoder enable
 board.set_encoder_enable(board.ALL)   
 # Set selected DC motor encoder disable: board.set_encoder_disable(board.ALL)
 # Set selected DC motor encoder reduction ratio, test motor reduction ratio is 43.8
 board.set_encoder_reduction_ratio(board.ALL, 43)
 # Set DC motor pwm frequency to 1000HZ
 board.set_moter_pwm_frequency(1000)

def dc_motor_start(duty):
 board.motor_movement([board.M1], board.CW, duty)

def dc_motor_stop():
 board.motor_stop([board.M1])

def dc_motor_give_card():
 dc_motor_start(25)
 time.sleep(0.5)
 dc_motor_stop()


def servo_motor_set_angle(angle):
 angle = angle
 if angle == "left":
  servo..set_servo_pulsewidth(servo_pin, 1000)
 if angle == "mid":
  servo..set_servo_pulsewidth(servo_pin, 1500)
 if angle == "right":
  servo..set_servo_pulsewidth(servo_pin, 2000)
 if angle == "off":
  servo..set_servo_pulsewidth(servo_pin, 0)