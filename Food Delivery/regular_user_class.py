# Author: Mahalinoro Razafimanjato
# Import the user class parent, drink and food for functions
from user_class import User
import drink_class
import food_class
import item_class

# Dictionary list for the regular user
regular_user = {}

# Global variables
user_choice_item = ""
amount = ""
itemtype = ""


# Regular User class which is the child of the User class
class RegularUser(User):
    # Method __init__ for the regular user
    def __init__(self, name, location, wallet):
        super().__init__(name)
        self.location = location
        self.wallet = wallet

    def __str__(self):
        pass

    # Method to update information for the instance variables
    def update_information(self, new_name, new_location):
        self.name = new_name
        self.location = new_location
        print("Information updated successfully.")
        return self.name, self.location

    # Method to add money to the wallet
    def add_money(self, updated_amount):
        self.wallet = self.wallet + updated_amount
        return self.wallet

    # Method to subtract money from the wallet
    def subtract_money(self, total_price):
        self.wallet = self.wallet - total_price
        return self.wallet


# Functions Section
def make_order():
    # This function will help the user to order a specific item
    # If the customer wants food/drink
    global user_choice_item
    global amount
    global itemtype
    itemtype = input(
        "Which type of item do you wish to order [drink/food]:  \n")
    if itemtype == "food":
        print("-------------- FOOD MENU ----------------")
        food_class.view_food_items()
        user_choice_item = input("Your food order:  \n")
        amount = int(input("Insert the quantity [ex: 1,2] :  \n"))
        confirmation = input("Are you confirming your order? [yes/no]:  \n")
        if confirmation == "yes":
            print("Order confirmed!")
        else:
            make_order()
    elif itemtype == "drink":
        print("--------------- DRINK MENU ---------------")
        drink_class.view_drink_items()
        user_choice_item = input("Your drink order:  \n")
        amount = int(input("Insert the quantity [ex: 1,2] :  \n"))
        confirmation = input("Are you confirming your order? [yes/no]:  \n")
        if confirmation == "yes":
            print("Order confirmed!")
        else:
            make_order()


def make_payments(username):
    # This function will subtract money from the wallet of the customer
    # It will be the payment part after ordering
    global itemtype
    global user_choice_item
    global amount
    if user_choice_item in food_class.food_item.keys():
        total_price = food_class.food_item[user_choice_item].calculate_total_price(user_choice_item, amount, itemtype)
        print("The total price is RWF" + str(total_price))
        if total_price <= regular_user[username].wallet:
            regular_user[username].subtract_money(total_price)
            user_location = regular_user[username].location
            item_class.delivery(user_location)
        else:
            print("Insufficient fund, cannot perform transaction!")
            confirmation = input("Do you wish to re-order again? [yes/no]: ")
            if confirmation == 'yes':
                make_order()
            else:
                exit()
    elif user_choice_item in drink_class.drink_item.keys():
        total_price = drink_class.drink_item[user_choice_item].calculate_total_price(user_choice_item, amount, itemtype)
        print("The total price is RWF " + str(total_price))
        if total_price <= regular_user[username].wallet:
            regular_user[username].subtract_money(total_price)
            user_location = regular_user[username].location
            item_class.delivery(user_location)
        else:
            print("Insufficient fund, cannot perform transaction!")
            confirmation = input("Do you wish to re-order again? [yes/no]: ")
            if confirmation == 'yes':
                make_order()
            else:
                exit()
    else:
        print("Error, Try again!")
        make_order()


def user_review():
    # After ordering and getting delivered, it will ask the user feedback and rating
    if user_choice_item in food_class.food_item.keys():
        user_rating_value = int(input("Please, rate the service [1-5]:  \n"))
        food_class.food_item[user_choice_item].user_rating(user_rating_value)
        user_feedback = input("Any feedback:  \n")
        food_class.food_item[user_choice_item].user_review(user_feedback)
        print("Thanks for your feedback!")
    elif user_choice_item in drink_class.drink_item.keys():
        user_rating_value = int(input("Please, rate the service [1-5]:  \n"))
        drink_class.drink_item[user_choice_item].user_rating(user_rating_value)
        user_feedback = input("Any feedback:  \n")
        drink_class.drink_item[user_choice_item].user_review(user_feedback)
        print("Thanks for your feedback!")
    else:
        print("Error, Try again!")
