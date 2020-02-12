# This is file containing the class for Bank Account
class BankAccount:
    # The __init__ method will create account instance automatically
    def __init__(self, account_number, account_name, account_pin, account_creation_day, account_creation_month,
                 account_creation_year, account_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_pin = account_pin
        self.account_creation_day = account_creation_day
        self.account_creation_month = account_creation_month
        self.account_creation_year = account_creation_year
        self.account_balance = account_balance

    def info_account(self):
        # This method will display the number and name of a specific account
        return "Account Number: " + self.account_number + "\n" + "Account Name: " + self.account_name

    def info_balance(self):
        # This method will return the account balance of a specific account
        return self.account_balance

    def withdraw(self):
        # This method will withdraw money from the account
        amount = int(input("Insert the amount of money you want to withdraw: "))
        if amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
            return self.account_balance
        else:
            print("Your balance is insufficient")

    def deposit(self):
        # This method will depose money in the account
        amount = int(input("Insert the amount of money you want to depose: "))
        self.account_balance = self.account_balance + amount
        return self.account_balance

