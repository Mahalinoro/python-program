# This file is for testing methods for current account
from current_account_class_file import CurrentAccount

# Test instance
test = CurrentAccount("101", "Hello World", 1245, 1, 11, 2019, 125000)

# Method test
print(test.info_account())
print(test.info_balance())
print(test.withdraw(100000))
print(test.deposit(1250))
print(test.calculate_interest())

# The methods call are working perfectly for the date
