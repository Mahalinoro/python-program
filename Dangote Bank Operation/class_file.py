# This is the class section for the program
# It contains all the classes we need to build the program
# From bank to client which all have their own attributes as well as the methods
# In this case, bank is the parent of the bank account and bank account is the parent of client


class Bank:
    def __init__(self, balance, id_number, name):
        self.name = "Dangote Capital Bank"
        self.capital = 1000000000000
        self.bank_account = BankAccount(balance, id_number, name)
        self.client = Client(id_number, name)


class BankAccount:
    def __init__(self, balance, id_number, name):
        self.client = Client(id_number, name)
        self.balance = balance

    def deposit(self, amount):
        # Method to depose money at the bank account
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        # Method to withdraw money at the bank account
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            print("Your balance is insufficient to perform this transaction!")
            self.balance = self.balance
            return self.balance

    def transfer(self, amount):
        # Method to transfer money from another account to another
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("$" + str(amount) + " has been successfully transferred.")
            return self.balance
        else:
            print("You balance is insufficient to perform this transaction!")
            transfer = self.balance
            return transfer

    def balance_info(self):
        # Method to check balance of the bank account
        return "Ledger available: $" + str(self.balance)


class Client:
    def __init__(self, id_number, name):
        self.id = id_number
        self.name = name
