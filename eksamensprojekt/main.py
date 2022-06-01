import os
from time import sleep
from RPi import GPIO
#os.system('python /home/master/eksamensprojekt/test.py')

print("Welcome to a perfect script for a scanner 😎")
led = 21 # 🪩
butt = 23 # 🍑
buzzkill = 27 # 😒
buzztime = 1023

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(butt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzkill, GPIO.OUT)
pi_pwm = GPIO.PWM(buzzkill,buzztime)
pi_pwm.start(0)

while True:
    if GPIO.input(butt) == GPIO.LOW:
        print("😬")
        GPIO.output(led,GPIO.HIGH)
        pi_pwm.ChangeDutyCycle(100)
        sleep(0.03)
        pi_pwm.ChangeDutyCycle(0)
        os.system('python /home/master/eksamensprojekt/test.py')
        GPIO.output(led,GPIO.LOW)
        pi_pwm.ChangeDutyCycle(100)
        sleep(0.03)
        pi_pwm.ChangeDutyCycle(0)
        sleep(0.1)
        pi_pwm.ChangeDutyCycle(100)
        sleep(0.03)
        pi_pwm.ChangeDutyCycle(0)
"""
Button:
    pin 22 gpio
LED:
    pin 21 gpio
Buzzer:
    pin 27 gpio
"""

#while True:
#    print("hello there")