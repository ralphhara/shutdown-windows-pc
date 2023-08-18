import os
import time

def shutdown_after_minutes(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    os.system("shutdown /s /f /t 1")
    
print("*********************************************************************************")
print("* This script will shutdown your computer after the amount of time you define.  *")
print("* Please enter how long time (in minutes) you want to wait before the shutdown. *")
print("* To abort the scritp, type cancel.                                             *")
print("*********************************************************************************")

while True:
    option = input("Enter time or cancel: ")
    if option == 'cancel':
        break
    elif __name__ == "__main__":
        try:
            minutes = int(option)
            shutdown_after_minutes(minutes)
        except ValueError:
            print("Invalid value. Please make sure you enter a integer number.\n")
            continue