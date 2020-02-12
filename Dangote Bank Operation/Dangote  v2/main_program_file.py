# This is the file containing the main program
# Importing the Current and Saving Account classes
from current_account_class_file import CurrentAccount
from saving_account_class_file import SavingAccount

# Algorithm explanation:
# Step1: Creating the parent class, the child classes and the methods corresponding
# Step2: Testing the method calls
# Step3: Creating the functions for the main program workflow

# Algorithm for the interest calculation:
# Using datetime to keep track on the date of account creation
# Taking the difference between today's date and creation date for saving withdraw and adding interest into the account

# This is the current account collection
current1 = CurrentAccount("101-01", "John Doe", 1234, 12, 1, 2019, 25000000)
current2 = CurrentAccount("101-02", "Sue Jane", 4589, 20, 10, 2018, 1500000)

current_account = [current1, current2]

# This is the saving account collection
saving1 = SavingAccount("102-01", "Annie Stone", 5782, 24, 1, 2019, 1850000)
saving2 = SavingAccount("102-02", "Patrick John", 7896, 25, 10, 2019, 20000000)

saving_account = [saving1, saving2]


def add_current_account():
    # This function will add a current account into the collection
    account_number = input("Insert account number [ex: 101-00]: ")
    account_name = input("Insert account name: ")
    account_pin = int(input("Insert account code pin [4 numbers]: "))
    account_creation_day = int(input("Insert account creation day [ex: 1 or 2 not 01 or 02]: "))
    account_creation_month = int(input("Insert account creation month [ex: 1 or 2 not 01 or 02]: "))
    account_creation_year = int(input("Insert account creation year [ex: 2019]: "))
    account_balance = int(input("Insert account balance: "))
    new_current_account = CurrentAccount(account_number, account_name, account_pin, account_creation_day,
                                         account_creation_month, account_creation_year, account_balance)
    current_account.append(new_current_account)
    print("Account created successfully")
    print(new_current_account.info_account())


def add_saving_account():
    # This function will add a saving account into the collection
    account_number = input("Insert account number [ex: 101-00]: ")
    account_name = input("Insert account name: ")
    account_pin = int(input("Insert account code pin [4 numbers]: "))
    account_creation_day = int(input("Insert account creation day [ex: 1 or 2 not 01 or 02]: "))
    account_creation_month = int(input("Insert account creation month [ex: 1 or 2 not 01 or 02]: "))
    account_creation_year = int(input("Insert account creation year [ex: 2017]: "))
    account_balance = int(input("Insert account balance: "))
    new_saving_account = SavingAccount(account_number, account_name, account_pin, account_creation_day,
                                       account_creation_month, account_creation_year, account_balance)
    saving_account.append(new_saving_account)
    print("Account created successfully")
    print(new_saving_account.info_account())


def delete_current_account():
    # This function will delete a selected current account in the list
    index = 0
    for account in current_account:
        print(str(index) + ". " + account.account_name)
        index += 1

    account_number = int(input("Insert the account number you wish to remove: "))
    selected_account = current_account[account_number]
    confirmation = input("Are you sure you want to remove " + selected_account.account_name + "?" + "[yes/y/no/n] :")
    if confirmation == "yes" or confirmation == "y":
        current_account.pop(account_number)
        print(selected_account.account_name + " removed successfully!")
    else:
        delete_current_account()


def delete_saving_account():
    # This function will delete a selected saving account in the list
    index = 0
    for account in saving_account:
        print(str(index) + ". " + account.account_name)
        index += 1

    account_number = int(input("Insert the account number you wish to remove: "))
    selected_account = saving_account[account_number]
    confirmation = input("Are you sure you want to remove " + selected_account.account_name + "?" + "[yes/y/no/n] :")
    if confirmation == "yes" or confirmation == "y":
        saving_account.pop(account_number)
        print(selected_account.account_name + " removed successfully!")
    else:
        delete_saving_account()


def restart():
    # This function will restart the main program depending on the user
    confirmation = input("Do you wish to perform another operation?(yes/y/no/n): ")

    if confirmation == "yes" or confirmation == "y":
        main()
    else:
        exit("See you soon for another operation!")


def print_menu():
    # This function will print the main menu for Dangote
    print("---------------------------------------------")
    print("                 BANK MENU                   ")
    print("---------------------------------------------")
    print("           1. Create an account              ")
    print("           2. Delete an account              ")
    print("           3. Other operations               ")
    print("---------------------------------------------")


loop = True


def main():
    # This is the main function containing the work flow of the whole program
    # Testing:
    # Scenario 1: What if Dangote want to remove an account that is not in the list?
    # Error 1: Yes, it gives us the index out of range error
    # Resolution 1: The only solution is to display all the available account before asking which one should be remove
    # Scenario 2: Can Dangote create more than one account? Is it updated in other operations after successful
    # operation?
    # Error 2: Yes, the last Dangote program couldn't create more than one account
    # Resolution 2: So I changed my work flow and now it is possible to create more than one account
    # Scenario 3: Is the interest applied in the balance when you want to check someone that has been there
    # for more than 1 month?
    # Error 3: There is no error, the interest is applied in the balance
    # Scenario 4: What about the saving account who can only withdraw after 6 months?
    # Error 4: There is no error, it works properly without issue
    while loop:
        print_menu()
        choice = int(input("Enter your choice [1-3]: "))

        if choice == 1:
            # Creating new account
            print("Create an account has been selected")
            true = True

            while true:
                print("------------------------------------")
                print("            ACCOUNT TYPE            ")
                print("------------------------------------")
                print("          1. Current Account        ")
                print("          2. Saving Account         ")
                print("------------------------------------")
                selection = int(input("Enter your choice [1-2]: "))
                if selection == 1:
                    add_current_account()
                    restart()
                elif selection == 2:
                    add_saving_account()
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 2:
            # Delete new account
            print("Delete an account has been selected")

            true = True

            while true:
                print("------------------------------------")
                print("            ACCOUNT TYPE            ")
                print("------------------------------------")
                print("          1. Current Account        ")
                print("          2. Saving Account         ")
                print("------------------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    delete_current_account()
                    restart()
                elif selection == 2:
                    delete_saving_account()
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 3:
            print("Other operations has been selected")

            true = True

            while true:
                print("------------------------------------")
                print("            ACCOUNT TYPE            ")
                print("------------------------------------")
                print("        1. Current Account          ")
                print("        2. Saving Account           ")
                print("------------------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    # This is the selection for current account
                    index = 0
                    for account in current_account:
                        print(str(index) + ". " + account.account_name)
                        index += 1
                    account_selected = int(input("Enter your choice : "))
                    selected = current_account[account_selected]
                    print(selected.account_name + ", Welcome!")
                    print("-------------------------------------")
                    print("           BANK OPERATION            ")
                    print("-------------------------------------")
                    print("          1. Withdrawal              ")
                    print("          2. Deposit                 ")
                    print("          3. Transfer                ")
                    print("          4. Balance info            ")
                    print("-------------------------------------")
                    menu_choice = int(input("Enter your operation choice [1-4]: "))
                    if menu_choice == 1:
                        # Withdrawal
                        amount = int(input("Insert amount [ex:1000] : "))
                        result = selected.withdraw(amount)
                        print("Ledger available: RWF" + str(result))
                        restart()
                    elif menu_choice == 2:
                        # Deposit
                        amount = int(input("Insert amount: "))
                        result = selected.deposit(amount)
                        print("Ledger available: RWF" + str(result))
                        restart()
                    elif menu_choice == 3:
                        # Transfer
                        index = 0
                        for account in current_account:
                            print(str(index) + ". " + account.account_name)
                            index += 1
                        transfer_person = int(input("Insert your choice: "))
                        transfer_person = current_account[transfer_person]
                        amount = int(input("Insert the amount you want to transfer: "))
                        if transfer_person != selected:
                            transfer_person.deposit(amount)
                            result = selected.withdraw(amount)
                            print("Ledger available: RWF" + str(result))
                            restart()
                        else:
                            print("Please re-insert valid id account! (Not yours)")
                            index = 0
                            for account in current_account:
                                print(str(index) + ". " + account.account_name)
                                index += 1
                            transfer_person = int(input("Insert the account id: "))
                            transfer_person = current_account[transfer_person]
                            amount = int(input("Insert the amount you want to transfer [number]: "))
                            transfer_person.deposit(amount)
                            result = selected.transfer(amount)
                            print("Ledger available: RWF" + str(result))
                            restart()
                    elif menu_choice == 4:
                        # Interest calculation
                        result = selected.calculate_interest()
                        print("Ledger available: RWF" + str(result))
                        restart()
                    else:
                        input("Wrong option selected. Enter any key to try again: ")
                elif selection == 2:
                    # This is the selection for saving account
                    index = 0
                    for account in saving_account:
                        print(str(index) + ". " +account.account_name)
                        index += 1
                    account_selected = int(input("Enter your choice : "))
                    selected = saving_account[account_selected]
                    print(selected.account_name + ", Welcome!")
                    print("-------------------------------------")
                    print("           BANK OPERATION            ")
                    print("-------------------------------------")
                    print("          1. Withdrawal              ")
                    print("          2. Deposit                 ")
                    print("          3. Transfer                ")
                    print("          4. Balance info            ")
                    print("-------------------------------------")
                    menu_choice = int(input("Enter your operation choice [1-4]: "))

                    if menu_choice == 1:
                        amount = int(input("Insert amount [ex:1000] : "))
                        result = selected.withdraw(amount)
                        print("Ledger available: RWF" + str(result))
                        restart()
                    elif menu_choice == 2:
                        amount = int(input("Insert amount: "))
                        result = selected.deposit(amount)
                        print("Ledger available: RWF" + str(result))
                        restart()
                    elif menu_choice == 3:
                        index = 0
                        for account in current_account:
                            print(str(index) + ". " + account.account_name)
                            index += 1
                        transfer_person = int(input("Insert your choice: "))
                        transfer_person = current_account[transfer_person]
                        amount = int(input("Insert the amount you want to transfer: "))
                        if transfer_person != selected:
                            transfer_person.deposit(amount)
                            result = selected.withdraw(amount)
                            print("Ledger available: RWF" + str(result))
                            restart()
                        else:
                            print("Please re-insert valid id account! (Not yours)")
                            index = 0
                            for account in saving_account:
                                print(str(index) + ". " + account.account_name)
                                index += 1
                            transfer_person = int(input("Insert the account id: "))
                            transfer_person = saving_account[transfer_person]
                            amount = int(input("Insert the amount you want to transfer [number]: "))
                            transfer_person.deposit(amount)
                            result = selected.transfer(amount)
                            print("Ledger available: RWF" + str(result))
                            restart()
                    elif menu_choice == 4:
                        result = selected.calculate_interest()
                        print("Ledger available: RWF" + str(result))
                        restart()
                    else:
                        input("Wrong option selected. Enter any key to try again: ")
        else:
            input("Wrong option selection. Enter any key to try again: ")


main()
