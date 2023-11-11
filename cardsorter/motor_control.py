import time
import RPi.GPIO as GPIO

from DFRobot_RaspberryPi_DC_Motor import THIS_BOARD_TYPE, DFRobot_DC_Motor_IIC as Board

#select bus 1, set address to 0x10
board = Board(1, 0x10)

servo_pin = 21
servo_motor_angle = None

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

def init_dc_motor():
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

def start_dc_motor(duty):
 board.motor_movement([board.M1], board.CW, duty)

def stop_dc_motor():
 board.motor_stop([board.M1])


def init_servo_motor():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(servo_pin, GPIO.OUT)
 servo_motor_angle = GPIO.PWM(servo_pin, 50)
 servo_motor_angle.start(5)

def set_servo_motor_angle(direction):
 if direction == left:
  servo_motor_angle.ChangeDutyCycle(2.5)
 if direction == middle:
  servo_motor_angle.ChangeDutyCycle(5)
 if direction == right:
  servo_motor_angle.ChangeDutyCycle(7.5)
 else:
  print("servo motor wrong direction")

def set_servo_motor_left():
 servo_motor_angle.ChangeDutyCycle(2.5)

def set_servo_motor_stop():
 servo_motor_angle.stop()
