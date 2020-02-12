print("Mahalinoro Razafimanjato" + "\n")

# Importing class from the function file
from function_file import *

# This is the upgraded version of Omondi car business
# This program is divided in 3 different files: the class file, the main file and the function file
# Car Business Operation function:
# Possibility for Omondi to add, view, remove, count revenue and rent times of each car in his collection

# Testing code:
# Scenario 1:
# What if the user add a new car then add another car? Is it going to be added to the new car collection?
# Yes, after testing the code it actually appends to the collection when you view all available cars
# I was expecting that it is going to override the value from the previous added car
# Scenario 2:
# What if the user remove accidentally a car that has been already removed?
# For my code, the it will give an error such as "Index Error: list index out of range"
# So, the best way to solve that issue is that to put the list of all available car before asking the user
# With that, the user can see which car can be removed from the collection
# Scenario 3:
# What if the user don't know the number ID Of the car that want to be rented?
# The same scenario goes for the remove a car, if the user get out of the range it gives the same error "Index Error"
# So, in order to facilitate the user with that we put the list of all available car to be rented on top
# With that, it will be easy and not hard it the program will not crash
# The same goes for all the other choices which I fixed for more user-friendly experience
# Scenario 4: What if the user input the wrong year format or input the incorrect format? In the add car section?
# After running the code: it will give ValueError: invalid literal for int() with base 10
# So in order to fix that, I have to indicate the user the format
# Scenario 5: What if the user doesn't want to remove the car anymore?
# To fix that issue, I add a new condition to handle confirmation so that the program knows when to remove/not remove.


car_operation()



