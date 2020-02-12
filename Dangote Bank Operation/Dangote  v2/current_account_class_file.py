# This file contains the current account class child
# Importing the parent class file
# Importing datetime for date manipulation
from bank_account_file import BankAccount
import datetime

# This is the current account class
class CurrentAccount(BankAccount):
    # The __init__ method for creating instances automatically
    def __init__(self, account_id, account_name, account_pin, account_creation_day, account_creation_month,
                 account_creation_year, account_balance):
        super().__init__(account_id, account_name, account_pin, account_creation_day, account_creation_month,
                         account_creation_year, account_balance)
        self.account_type = "Current Account"
        self.interest = 0.01

    def info_account(self):
        # Method for account information display
        return "Account Number: " + self.account_number + "\n" + "Account Name: " + self.account_name + "\n" \
               + "Account Type: " + self.account_type

    def info_balance(self):
        # Method for account balance display
        return "Balance: " + str(self.account_balance)

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
            return self.account_balance
        else:
            print("Your balance is insufficient")

    def deposit(self, amount):
        # Method to depose money to the account
        self.account_balance = self.account_balance + amount
        return self.account_balance

    def calculate_interest(self):
        # Method to calculate interest for the account
        # Getting today's date with datetime
        date_today = datetime.date.today()
        # Formatting the information from the instance into date format with datetime
        date_creation = datetime.datetime(self.account_creation_year, self.account_creation_month,
                                          self.account_creation_day)
        # Getting the difference by subtracting the month
        difference_month = date_today.month - date_creation.month
        # Getting the difference by subtracting the year
        difference_year = date_today.year - date_creation.year
        # Control flow to get the interest, if the account is greater or equal to 1 and the year is 0 or greater
        # or equal to 1 then the balance will add onto the amount multiplied by the interest
        # if not then nothing happens, the balance remain the same as from the creation date
        if difference_month >= 1 and difference_year == 0 or difference_year >= 1:
            amount = self.account_balance * self.interest
            self.account_balance = self.account_balance + amount
            return self.account_balance
        else:
            return self.account_balance
