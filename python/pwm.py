import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

class pwm_control():
    def __init__(self):
        self.right_pwm_pin = 32            #Select Pin  
        self.left_pwm_pin = 33             
        self.right_pwm_en_1 = 11
        self.left_pwm_en_1 = 13
        self.right_pwm_en_2 = 15
        self.left_pwm_en_2 = 16
        self.car_direction_right = True
        self.car_direction_left = True

        self.isBusy = True
        self.right_pwm_value = 0
        self.left_pwm_value = 0
        self.isClose = 0
        
        GPIO.setwarnings(False)         #GPIO PIN Setup
        GPIO.setmode(GPIO.BOARD)        
        GPIO.setup(self.right_pwm_pin,GPIO.OUT)
        GPIO.setup(self.left_pwm_pin,GPIO.OUT)
        GPIO.setup(self.right_pwm_en_1,GPIO.OUT)
        GPIO.setup(self.left_pwm_en_1,GPIO.OUT)
        GPIO.setup(self.right_pwm_en_2,GPIO.OUT)
        GPIO.setup(self.left_pwm_en_2,GPIO.OUT)

        self.right_pwm = GPIO.PWM(self.right_pwm_pin,1000)      #Right PWM Setup
        self.right_pwm.start(0)             
        self.left_pwm = GPIO.PWM(self.left_pwm_pin,1000)       #Left PWM Setup
        self.left_pwm.start(0)

                   
    def right_pwm_control(self):          #Thread for Right PWM
        while self.isBusy:
            self.direction_right()
            self.right_pwm.ChangeDutyCycle(self.pwm_value_control(self.right_pwm_value))
            #print("Sağ "+str(self.pwm_value_control(self.right_pwm_value))) 
            sleep(0.1)
        self.close_check()

    def left_pwm_control(self):           #Thread for Left PWM
        while self.isBusy:
            self.direction_left()
            self.left_pwm.ChangeDutyCycle(self.pwm_value_control(self.left_pwm_value)) 
            #print("Sol "+str(self.pwm_value_control(self.left_pwm_value))) 
            sleep(0.1)
        self.close_check()

    def pwm_value_control(self,pwm_value):  #Control PWM value for unexpected situations
        if pwm_value < 0:
            pwm_value = 0
        elif pwm_value > 100:
            pwm_value = 100
        return pwm_value
    def direction_right(self):
        if self.car_direction_right == True:
            GPIO.output(self.right_pwm_en_1,GPIO.HIGH)
            GPIO.output(self.right_pwm_en_2,GPIO.LOW)
            #print("Sağ ileri")
            pass
        else:
            GPIO.output(self.right_pwm_en_1,GPIO.LOW)
            GPIO.output(self.right_pwm_en_2,GPIO.HIGH)
            #print("Sağ geri")
            pass
    def direction_left(self):
        if self.car_direction_left == True:
            GPIO.output(self.left_pwm_en_1,GPIO.HIGH)
            GPIO.output(self.left_pwm_en_2,GPIO.LOW)
            #print("Sol ileri")
            pass
        else:
            GPIO.output(self.left_pwm_en_1,GPIO.LOW)
            GPIO.output(self.left_pwm_en_2,GPIO.HIGH)
            #print("Sol geri")
            pass
    def close_check(self):
        self.isClose = self.isClose + 1
        if(self.isClose==2):
            GPIO.cleanup()
            print("Closed")

    def run(self):                                  #Run Threads
        Thread(target=self.right_pwm_control).start()
        Thread(target=self.left_pwm_control).start()

