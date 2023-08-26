import time
import write_type_animations
import os
import datetime
from colorama import Fore, Back, Style
import colorama
colorama.init()
time.sleep(0.30)
class PyDev():
    def __init__(self):
        self.user_input = input("Enter To Generate PyDev's Response: ")
        self.user_inputs = self.user_input.removesuffix(" ")
        self.user_input_lower = self.user_inputs.lower()
        self.currenttime = datetime.datetime.now()
        self.currenthours = self.currenttime.hour
        self.Response_Genertor()

    def Response_Genertor(self):
        if self.user_input_lower == "":
                write_type_animations.write_like_gpt("I'm sorry, I didn't receive a question or request from you. How can I assist you today?")

        elif "bye" in self.user_input_lower and len(self.user_input_lower) <= 20:
            write_type_animations.write_like_gpt("Goodbye! Don't hesitate to ask if you have any questions in the future.")

        elif self.user_input == f"./run {self.user_input[6:]}":
            os.system("cls")
            # Execute the code
            try:
                exec(self.user_input[6:])
            except Exception as e:
                print("Error:", e)

        elif "time" in self.user_input_lower and len(self.user_input_lower) <= 25:
            if "what" in self.user_input_lower :
                write_type_animations.write_like_gpt("The current time and date is: ")
                write_type_animations.write_like_gpt(f"Year: {self.currenttime.year}")
 
                write_type_animations.write_like_gpt(f"Month: {self.currenttime.month}")
 
                write_type_animations.write_like_gpt(f"Day: {self.currenttime.day}")
 
                write_type_animations.write_like_gpt(f"Hour: {self.currenttime.hour}")
 
                write_type_animations.write_like_gpt(f"Minute: {self.currenttime.minute}")
 
                write_type_animations.write_like_gpt(f"Second: {self.currenttime.second}")

                if self.currenttime.strftime("%p") == "AM":
                    write_type_animations.write_like_gpt(f"AM/PM: {self.currenttime.strftime('%p')}")

                elif self.currenttime.strftime("%p") == "PM":
                    write_type_animations.write_like_gpt(f"PM/AM: {self.currenttime.strftime('%p')}")

                write_type_animations.write_like_gpt("over all time and date is: ")

                write_type_animations.write_like_gpt(str(self.currenttime) +" "+ str(self.currenttime.strftime("%p")), "")
            
while True:
    try:
        pydev = PyDev()
    except:
        os.system("cls")
        print(Back.LIGHTYELLOW_EX + Fore.MAGENTA + "________________________________________________________________________________________________")
        print("                                                                                            ")
        print("                                                                                            ")
        print("                                                                                            ")
        print("                                                                                            ")
        print("                                                                                            ")
        write_type_animations.write_like_gpt("Warning - PyDev is not available yet\ntry to reconnect or try later.".center(100))
        break
write_type_animations.write_in_ascii("Thanks for using PyDev.".center(100))
print(Back.LIGHTYELLOW_EX + Fore.MAGENTA + "                                                                                            ")
print("                                                                                            ")
print("                                                                                            ")
print("                                                                                            ")
print("                                                                                            ")
print("________________________________________________________________________________________________")
