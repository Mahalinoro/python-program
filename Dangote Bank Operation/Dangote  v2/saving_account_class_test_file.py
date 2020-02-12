# This file contains the method calls testing for saving account
from saving_account_class_file import SavingAccount

test = SavingAccount("102", "Hello World", 1245, 1, 1, 2019, 125000)

# Method calls testing
print(test.info_account())
print(test.info_balance())
print(test.withdraw(1250))
print(test.deposit(1200))
print(test.calculate_interest())

# The method calls are working perfectly as well as calculating the interest and withdrawing money after 6 months
