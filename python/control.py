import python.pwm as pwm

class control():
    def __init__(self):
        self.pc = pwm.pwm_control()
        self.speed = 50
    def forward(self):
        self.pc.car_direction_right = True
        self.pc.car_direction_left = True
        self.pc.right_pwm_value = self.speed
        self.pc.left_pwm_value = self.speed
        print("forward")
    def bacward(self):
        self.pc.car_direction_right = False
        self.pc.car_direction_left = False
        self.pc.right_pwm_value = self.speed
        self.pc.left_pwm_value = self.speed
        print("backward")
    def right(self):
        self.pc.car_direction_right = False
        self.pc.car_direction_left = True
        self.pc.right_pwm_value = self.speed
        self.pc.left_pwm_value = self.speed
        print("right")
    def left(self):
        self.pc.car_direction_right = True
        self.pc.car_direction_left = False
        self.pc.right_pwm_value = self.speed
        self.pc.left_pwm_value = self.speed
        print("left")
    def scan_360(self):
        self.pc.car_direction_right = False
        self.pc.car_direction_left = True
        self.pc.right_pwm_value = 35
        self.pc.left_pwm_value = 35
        print("360")
    def stop(self):
        self.pc.right_pwm_value = 0
        self.pc.left_pwm_value = 0
        print("stoped")
    def run(self):
        self.pc.run()
