import time
import RPi.GPIO as GPIO
import logging
import pigpio
from gpiozero import Servo

from DFRobot_RaspberryPi_DC_Motor import THIS_BOARD_TYPE, DFRobot_DC_Motor_IIC as Board

#select bus 1, set address to 0x10
board = Board(1, 0x10)

#servo_pin = 21
servo = Servo(21)

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
 # Set selected DC motor encoder disable:              
 # board.set_encoder_disable(board.ALL)

 # Set selected DC motor encoder reduction ratio, test motor reduction ratio is 43.8
 board.set_encoder_reduction_ratio(board.ALL, 43)

 # Set DC motor pwm frequency to 1000HZ
 board.set_moter_pwm_frequency(1000)

def dc_motor_start(duty):
 board.motor_movement([board.M1], board.CW, duty)

def dc_motor_stop():
 board.motor_stop([board.M1])

def dc_motor_give_card():
 start_dc_motor(25)
 time.sleep(0.5)
 stop_dc_motor()



def servo_motor_init():
 #GPIO.setmode(GPIO.BCM)
 #GPIO.setup(servo_pin, GPIO.OUT)
 #global servo_motor
 #servo_motor = GPIO.PWM(servo_pin, 50)
 #servo_motor.start(5)
 global servo_pwm
 servo_pwm = pigpio.pi()
 servo_pwm.set_mode(servo_pin, pigpio.OUTPUT)
 pwm.set_PWM_frequency( servo_pin, 50 )

def servo_motor_set_angle(angle):
 angle = angle
 if angle == "left":
  servo.min()
 if angle == "middle":
  servo.mid()
 if angle == "right":
  servo.max()


#def servo_motor_set_left():
# servo_motor_angle.ChangeDutyCycle(5)

#def servo_motor_set_middle():
# servo_motor_angle.ChangeDutyCycle(7.5)

#def servo_motor_set_right():
# servo_motor_angle.ChangeDutyCycle(10)

#def servo_motor_stop():
# servo_motor_angle.stop()
# GPIO.cleanup()