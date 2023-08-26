from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import time
# import write_type_animations
import os
import datetime
time.sleep(0.30)
class PyDev(QMainWindow):
    def __init__(self):
        self.user_input = input("Enter To Generate PyDev's Response: ")
        self.user_inputs = self.user_input.removesuffix(" ")
        self.user_input_lower = self.user_inputs.lower()
        self.currenttime = datetime.datetime.now()
        self.currenthours = self.currenttime.hour
        self.Response_Genertor()

    def Response_Genertor(self):
        if self.user_input_lower == "":
                ("I'm sorry, I didn't receive a question or request from you. How can I assist you today?")

        elif "bye" in self.user_input_lower and len(self.user_input_lower) <= 20:
            ("Goodbye! Don't hesitate to ask if you have any questions in the future.")

        elif self.user_input == f"./run {self.user_input[6:]}":
            os.system("cls")
            # Execute the code
            try:
                exec(self.user_input[6:])
            except Exception as e:
                print("Error:", e)

        elif "time" in self.user_input_lower and len(self.user_input_lower) <= 25:
            if "what" in self.user_input_lower :
                ("The current time and date is: ")
                (f"Year: {self.currenttime.year}")
 
                (f"Month: {self.currenttime.month}")
 
                (f"Day: {self.currenttime.day}")
 
                (f"Hour: {self.currenttime.hour}")
 
                (f"Minute: {self.currenttime.minute}")
 
                (f"Second: {self.currenttime.second}")

                if self.currenttime.strftime("%p") == "AM":
                    (f"AM/PM: {self.currenttime.strftime('%p')}")

                elif self.currenttime.strftime("%p") == "PM":
                    (f"PM/AM: {self.currenttime.strftime('%p')}")

                ("over all time and date is: ")

                (str(self.currenttime) +" "+ str(self.currenttime.strftime("%p")), "")
            
while True:
    try:
        pydev = PyDev()
    except:
        os.system("cls")