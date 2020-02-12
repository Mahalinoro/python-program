print("Mahalinoro Razafimanjato" + "\n")

from class_file import *

# This program is about controlling the elevator at Kigali Heights
# By controlling it means: opening, closing and knowing the status of the elevator (moving, floor number...)

# Testing code:
# Scenario 1: What if the user input the number of floor which is out of the range?
# For example the room has 9th floor and the user input 10, it will give us IndexError: out of the range
# So in order to fix that, I used condition to handle the error and it will restart again if it is out of the range
# Scenario 2: What if the user input  a string?
# Since I already put the range of elevator, the user will know what to put so it is more user friendly in that case
# But when I tested the code, it will give ValueError: invalid literal for int() with base 10
# So the program will crash, that is why I put the range of floors the user can only select in the user input
# For this program specifically, there is no other issue that can crash the program
# In general, the code is running perfectly

print("------- WELCOME TO KIGALI HEIGHTS ELEVATOR --------")
# Creating the instance building
building_one = Building()
# Calling the instance method run for the main program to work
building_one.run()


