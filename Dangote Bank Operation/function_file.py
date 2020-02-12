from class_file import *

# This file is for the function file related to Dangote bank



# This is the list of all clients at the bank
# For now it contains only five account holder but it can be added more than that if a new client opened an account

client_one = Bank(125000, 0, "Richard")
client_two = Bank(5000000, 1, "Eric")
client_three = Bank(1000000, 2, "Charles")
client_four = Bank(2000000, 3, "Wendy")
client_five = Bank(350000, 4, "Patricia")
account_holder = [client_one, client_two, client_three, client_four, client_five]


def run_operation(selected_account):
    # This is the main operation for the bank
    # The user interface which the user can withdraw, depose and check balance
    # It will ask the id account of the user for now - just to identify it which nth element of the list it should take

    service_choice = int(input(
        """-------------- Service Available --------------
                1. Withdrawal
                2. Deposit
                3. Balance Check 
                4. Transfer money 
          Select transaction service: """))
    if service_choice == 1:
        amount = int(input("How much do you want to withdraw? [number]: "))
        result = selected_account.bank_account.withdraw(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 2:
        amount = int(input("How much do you want to depose? [number]: "))
        result = selected_account.bank_account.deposit(amount)
        print("Ledger available: $" + str(result))
        restart(selected_account)
    elif service_choice == 3:
        print(selected_account.bank_account.balance_info())
        restart(selected_account)
    elif service_choice == 4:
        index = 0
        for x in account_holder:
            print(str(index) + ". " + x.client.name)
            index += 1
        transfer_person = int(input("Insert the account id: "))
        transfer_person = account_holder[transfer_person]
        amount = int(input("Insert the amount you want to transfer [number]: "))
        if transfer_person != selected_account:
            result_one = transfer_person.bank_account.deposit(amount)
            result_two = selected_account.bank_account.transfer(amount)
            print("Ledger available: $" + str(result_two))
        else:
            print("Please re-insert valid id account! (Not yours)")
            index = 0
            for x in account_holder:
                print(str(index) + ". " + x.client.name)
                index += 1
            transfer_person = int(input("Insert the account id: "))
            transfer_person = account_holder[transfer_person]
            amount = int(input("Insert the amount you want to transfer [number]: "))
            result_one = transfer_person.bank_account.deposit(amount)
            result_two = selected_account.bank_account.transfer(amount)
        restart(selected_account)
    else:
        print("Error: please try again!")
        run_operation(selected_account)


def restart(selected_account):
    # This function is used to restart and perform another transaction
    restart = input("Do you wish to perform another transaction?(yes/no): ")
    if restart == "yes":
        run_operation(selected_account)
    else:
        exit("Thank your for using Dangote Bank!")


def create_account():
    # This function will create a new bank account in the list
    balance = int(input("Insert the amount of money you wish to put in the new account: "))
    id_number = int(input("Insert an id corresponding to the new account [ex: 5, 6, ...]: "))
    name = input("Insert the name of the account holder: ")
    new_account = Bank(balance, id_number, name)
    account_holder.append(new_account)
    print("Account created successfully!")
