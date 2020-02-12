print("Mahalinoro Razafimanjato" + "\n")

# importing the class and functions from the function file
from function_file import *

# This is the main function which will run the program
# For now it is a simple program which doesn't take into consideration fees or any other extra variables
# It is a basic program which only have withdraw, deposit and check balance available

# Testing Code:
# Scenario 1: What if Omondi want to perfom operation on the new account created?
# After testing the code, created a new account and then perform operation, it works properly without error
# Scenario 2: What if Omondi withdraw money which is greater than the amount in the balance?
# After testing the code for a specific account on the list, it gave us negative number which shouldn't be there
# So for that, I added a condition that handle the error. Now it works properly.
# Scenario 3: What if Omondi selected the user id of the the same account while transfer money?
# Eventually when you execute the code it will not give you error but it will add that amount to the current account
# Which is not what we want, so I added an if statement to handle that so that transfer is not the same as deposit
# Scenario 4: What if Omondi doesn't remember the client account number?
# From the beginning, I assume that while creating an account they have to remember that ID in order to access it
# But since we are talking about Omondi, I may forget the ID he wants to access
# So for that, I added a list of the user and their ID number to ease the process for all operations that need that
# Scenario 5: What if Omondi input amount in letters instead of numbers?
# After running the code and trying that it will give us error with the int() and str() format issue
# But in order to avoid that, I added after input the specification which is the number
# So in that case, it will help the user to give us the correct input

print("--------------- WELCOME TO DANGOTE CAPITAL BANK --------------")
omondi_input = int(input("""Operation you want to perform: 
                            1. Create an account
                            2. Other operation on clients
                            Please select your choice: """))
if omondi_input == 1:
    create_account()
elif omondi_input == 2:
    index = 0
    for x in account_holder:
        print(str(index) + ". " + x.client.name)
        index += 1
    account_id = int(input("Please insert the account id: "))
    selected_account = account_holder[account_id]
    print("Welcome to our service, " + selected_account.client.name + "!")
    run_operation(selected_account)
else:
    print("Please, you can only select between 1 and 2!")
    print("Please, try again!")
omondi_input = int(input("""Operation you want to perform: 
                               1. Create an account
                               2. Other operation on clients
                               Please select your choice: """))
if omondi_input == 1:
    create_account()
elif omondi_input == 2:
    account_id = int(input("Please insert your account id: "))
    selected_account = account_holder[account_id]
    print("Welcome to our service, " + selected_account.client.name + "!")
    run_operation(selected_account)



