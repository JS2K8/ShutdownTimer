# Imported Modules
import os

# Global Variables
choice = ""
choice_intitial = ""
unit = ""
unit_initial = ""
value = ""

# Bold
class colour:
    BOLD = '\033[1m'
    END = '\033[0m'

def start():
    print("Welcome to Shutdown Timer!")
    input("Press Enter to continue...")
    option()

def cancel():
    loop = 1
    print("This is your chance to cancel the timer. If you would like to do this enter 'cancel' below. Enter anything else to continue with the timer.")
    cancel = input(">>> ")
    if cancel.lower() == "cancel":
        os.system("shutdown /a")
        while loop == 1:
            print("Timer cancelled. Would you like to set another timer? y/n")
            redo = input(">>> ")
            if redo.lower() == "y" or redo.lower() == "yes":
                start()
            elif redo.lower() == "n" or redo.lower() == "no":
                print("\nThank you for using Shutdown Timer!")
                loop = 0
            else:
                print("Invalid option.")
    else:
        print("\nThank you for using Shutdown Timer!")

def process():
    global value
    global choice_intitial
    global unit_initial
    global choice
    global unit
    value2 = ""
    if unit_initial == "s":
        os.system(f"shutdown /{choice_intitial} /t {value}")
    elif unit_initial == "m":
        value2 = value * 60
        os.system(f"shutdown /{choice_intitial} /t {value2}")
    else:
        value2 = value * 3600
        os.system(f"shutdown /{choice_intitial} /t {value2}")
    print(colour.BOLD + f"\nYour computer will {choice} in {str(value)} {unit}.\n" + colour.END)
    cancel()

def time():
    global unit
    global value
    global unit_initial
    loop = 1
    loop2 = 1
    while loop == 1:
        print("""
            You can use either seconds, minutes, or hours.
            What unit of time would you like to use? S/M/H
            """)
        unit2 = input(">>> ")
        if unit2.lower() == "s" or unit2.lower == "seconds":
            unit = "seconds"
            unit_initial = "s"
            loop = 0
        elif unit2.lower() == "m" or unit2.lower() == "minutes":
            unit = "minutes"
            unit_initial = "m"
            loop = 0
        elif unit2.lower() == "h" or unit2.lower() == "hours":
            unit = "hours"
            unit_initial = "h"
            loop = 0
        else:
            print("Invalid option.")
    while loop2 == 1:
        print(f"How many {unit} until {choice}?")
        val = input(">>> ")
        try:
            value = int(val)
            loop2 == 0
            process()
            exit()
        except ValueError:
            print("Please enter a whole number.")

def option():
    global choice
    global choice_intitial
    loop = 1
    while loop == 1:
        print("Would you like to shutdown or restart? S/R")
        user_option = input(">>> ")
        if user_option.lower() == "s" or user_option.lower() == "shutdown" or user_option.lower() == "shut down":
            loop = 0
            choice = "shutdown"
            choice_intitial = "s"
            time()
        elif user_option.lower() == "r" or user_option.lower() == "restart":
            loop = 0
            choice = "restart"
            choice_intitial = "r"
            time()
        else:
            print("Invalid option.")

start()

# # Cancel
# os.system("shutdown /a")