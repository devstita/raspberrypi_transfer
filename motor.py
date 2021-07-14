import GPi.GPIO as GPIO
from time import sleep

left_front_pin = 22
right_front_pin = 23

left_back_pin = 24
right_back_pin = 25

duty_cycle = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_front_pin, GPIO.OUT)
GPIO.setup(right_front_pin, GPIO.OUT)
GPIO.setup(left_back_pin, GPIO.OUT)
GPIO.setup(right_back_pin, GPIO.OUT)

left_front_pwm = GPIO.PWM(left_front_pin, 100)
right_front_pwm = GPIO.PWM(right_front_pin, 100)
left_back_pwm = GPIO.PWM(left_back_pin, 100)
right_back_pwm = GPIO.PWM(right_back_pin, 100)


def forward():
    stop()
    left_front_pwm.start(100)
    right_front_pwm.start(100) 


def right(): 
    stop()
    left_front_pwm.start(100)
    right_front_pwm.start(20)


def left(): 
    stop()
    left_front_pwm.start(20)
    right_front_pwm.start(100)


def stop(): 
    left_front_pwm.stop()
    right_front_pwm.stop()
    left_back_pwm.stop()
    right_back_pwm.stop()

