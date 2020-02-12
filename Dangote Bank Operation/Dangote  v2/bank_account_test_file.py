# This file contains the test for bank account class
from bank_account_file import BankAccount

# Test instance
test = BankAccount("101", "Hello World", 1245, 2, 11, 2018,2000000)

# Test method calls
print(test.info_account())
print(test.info_balance())
print(test.withdraw())
print(test.deposit())

# After fixing some errors about comparison, it works perfectly now

