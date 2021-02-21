import cv2 
import time
import numpy as np
from pyzbar import pyzbar

# Blue 91 114 120 115 255 255
# Yellow 16 56 135 30 255 255
# Green 40 70 150 80 255 255
# Red (0 100 0 10 255 255) (170 80 0 180 255 255)

class scanner:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.kernel = np.ones((5,5),np.uint8)
        self.founded_colors = ["0","0","0","0"]   # Red, Green, Blue, Yellow
        self.lower_blue = (91, 114, 120)
        self.upper_blue = (115, 255, 255)
        self.lower_yellow = (16, 56, 135)
        self.upper_yellow = (30, 255, 255)
        self.lower_green = (40, 70, 150)
        self.upper_green = (80, 255, 255)
        self.lower_red_1 = (0, 100, 0) 
        self.lower_red_2 = (170, 100, 0)
        self.upper_red_1 = (10, 255, 255)
        self.upper_red_2 = (180, 255, 255)
        self.hsv = []

    def reseter(self):
        self.founded_colors = ["0", "0", "0", "0"]
    def qr_scan(self,frame):
        qrs = pyzbar.decode(frame)
        if qrs: 
            qrData = qrs[0].data.decode("utf-8")
            if qrData == "START_STOP":
                return 1
            else:
                return 0
        else:
            return 0 
    def found_red(self):
        lower_red = cv2.inRange(self.hsv, self.lower_red_1, self.upper_red_1)
        upper_red = cv2.inRange(self.hsv, self.lower_red_2, self.upper_red_2) 
        mask = lower_red + upper_red
        if self.find_area(mask):
            self.founded_colors[0] = "1"
            print("red")
    def found_green(self):
        mask = cv2.inRange(self.hsv, self.lower_green, self.upper_green) 
        if self.find_area(mask):
            self.founded_colors[1] = "1"
            print("green")
    def found_blue(self):
        mask = cv2.inRange(self.hsv, self.lower_blue, self.upper_blue) 
        if self.find_area(mask):
            self.founded_colors[2] = "1"
            print("blue")
    def found_yellow(self):
        mask = cv2.inRange(self.hsv, self.lower_yellow, self.upper_yellow) 
        if self.find_area(mask):
            self.founded_colors[3] = "1"
            print("yellow")
    def find_area(self,mask):
        mask = cv2.erode(mask,self.kernel)
        counters, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in counters:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            if area > 3000:
                cv2.drawContours(mask,[approx],0,(0,0,255),5)
                if len(approx) == 4:
                    return 1 
        return 0

    def scan(self):
        self.reseter()
        start_time = time.time()
        while True:
            ret , frame = self.cap.read()
            if ret:
                self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                self.found_red()
                self.found_green()
                self.found_blue()
                self.found_yellow()
                if ((time.time() - start_time) > 3 and self.qr_scan(frame)):
                    break
