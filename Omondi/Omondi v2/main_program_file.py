# This is the main program file
# Importing the class files for Car and Moto
from car_class_file import Car
from moto_class_file import Moto

# Algorithm explanation:
# Step1: Creating the vehicle, car and moto classes
# Step2: Creating the methods and testing the method calls
# Step3: Creating the instances for the car collection and moto collection
# Step4: Creating view, add and remove vehicles functions
# Step5: Creating the main function containing the work flow of the main program

# Carbon footprint algorithm:
# To get the number of year released: 2019 - year_released
# To get the average miles yearly: mean(miles yearly)
# To get the gallons per mile: total gallons divided by total miles yearly
# To get the carbon per gallon: total carbon divided by total gallons yearly
# The formula of carbon footprint:
# Car = number of year since released * 12000(average miles per car yearly)*15 (gallons per mile) *
# 9 (grams of co2 per gallon)
# Moto = Number of year since released*10000(average miles yearly)*2(gallons per mile)*9(grams /gallon)


# This is the collection of cars
car1 = Car("Toyota", 2012, 2015, 0, "5212 TAB", 0, 0, 0, 0, 0)
car2 = Car("Aspire", 2015, 2016, 0, "1278 TU", 0, 0, 0, 0, 0)
car3 = Car("RAV4", 2012, 2013, 0, "4578 TAB", 0, 0, 0, 0, 0)
car4 = Car("BMW", 2011, 2012, 0, "2888 WWT", 0, 0, 0, 0, 0)
car5 = Car("Chevrolet", 2014, 2015, 0, "5692 TAK", 0, 0, 0, 0, 0)

car_collection = [car1, car2, car3, car4, car5]

# This is the collection of motos
moto1 = Moto("Yamaha H-20", 2016, 2017, 0, "125 KT", 0, 0, 0, 0, 0, 0)
moto2 = Moto("Suzuki M-10", 2014, 2016, 0, "454 TA", 0, 0, 0, 0, 0, 0)
moto3 = Moto("Honda 400", 2015, 2016, 0, "101 MK", 0, 0, 0, 0, 0, 0)
moto4 = Moto("Yamaha M-2", 2014, 2015, 0, "142 TB", 0, 0, 0, 0, 0, 0)
moto5 = Moto("Honda T-200", 2014, 2016, 0, "578 MU", 0, 0, 0, 0, 0, 0)

moto_collection = [moto1, moto2, moto3, moto4, moto5]


def view_car():
    # This function will display the car collection
    index = 0
    for car in car_collection:
        print(str(index) + ". " + car.info())
        index += 1


def view_car_details():
    # This function will display a detailed information of a specific car
    index = 0
    for car in car_collection:
        print(str(index) + ". " + car.model)
        index += 1

    car_number = int(input("The car number you wish to see in details [ex: 1]: "))
    selected_car = car_collection[car_number]
    print(selected_car.info_details())


def view_moto():
    # This function will display the moto collection
    index = 0
    for moto in moto_collection:
        print(str(index) + ". " + moto.info())
        index += 1


def view_moto_details():
    # This function will display a detailed information of a specific moto
    index = 0
    for moto in moto_collection:
        print(str(index) + ". " + moto.model)
        index += 1

    moto_number = int(input("The moto number you wish to see in details [ex: 1]: "))
    selected_moto = car_collection[moto_number]
    print(selected_moto.info_details())


def add_car():
    # This function will add a new car in the collection
    model = input("Insert the car model: ")
    year_released = int(input("Insert the year when it was released (YYYY): "))
    year_acquired = int(input("Insert the year when it was acquired (YYYY): "))
    rent_time = int(input("Insert the number of times it has been rented: "))
    plate_number = input("Insert the plate number: ")
    revenue = int(input("Insert the revenue made from it [number]: "))
    miles = int(input("Insert the total miles made yearly [number]: "))
    gallons = int(input("Insert the liters of gallons consumed yearly [number]: "))
    carbon = int(input("Insert the total grams of CO2 emitted yearly [number]: "))
    carbon_footprint = int(input("Insert the carbon footprint [number]: "))

    new_car = Car(model, year_released, year_acquired, rent_time, plate_number, revenue, miles, gallons,
                  carbon, carbon_footprint)
    car_collection.append(new_car)
    print("\n")
    print(new_car.model + " added successfully:")
    print(new_car.vehicle_info())


def add_moto():
    # This function will add a new moto in the collection
    model = input("Insert the moto model: ")
    year_released = int(input("Insert the year when it was released (YYYY): "))
    year_acquired = int(input("Insert the year when it was acquired (YYYY): "))
    rent_time = int(input("Insert the number of times it has been rented: "))
    plate_number = input("Insert the plate number: ")
    revenue = int(input("Insert the revenue made from it [number]: "))
    helmet_number = int(input("Insert the number of helmets available: "))
    miles = int(input("Insert the total miles made yearly [number]: "))
    gallons = int(input("Insert the liters of gallons consumed yearly [number]: "))
    carbon = int(input("Insert the total grams of CO2 emitted yearly [number]: "))
    carbon_footprint = int(input("Insert the carbon footprint [number]: "))
    new_moto = Moto(model, year_released, year_acquired, rent_time, plate_number, revenue, helmet_number, miles,
                    gallons, carbon, carbon_footprint)

    moto_collection.append(new_moto)
    print("\n")
    print(new_moto.model + " added successfully:")
    print(new_moto.vehicle_info())


def remove_car():
    # This function will remove a selected car from the collection
    index = 0
    for car in car_collection:
        print(str(index) + ". " + car.model)
        index += 1
    car_number = int(input("The car number you wish to remove [ex: 1]: "))
    selected_car = car_collection[car_number]
    confirmation = input("Are you sure you want to remove " + selected_car.model + "? [yes/y/no] :")

    if confirmation == "yes" or confirmation == "y":
        removed_car = car_collection.pop(car_number)
        print(removed_car.model + " removed successfully!")
    else:
        remove_car()


def remove_moto():
    # This function will remove a selected moto from the collection
    index = 0
    for moto in moto_collection:
        print(str(index) + ". " + moto.model)
        index += 1
    moto_number = int(input("The moto number you wish to remove [ex: 1]: "))
    selected_moto = moto_collection[moto_number]
    confirmation = input("Are you sure you want to remove " + selected_moto.model + "? [yes/y/no] :")

    if confirmation == "yes" or confirmation == "y":
        removed_moto = moto_collection.pop(moto_number)
        print(removed_moto.model + " removed successfully!")
    else:
        remove_moto()


def print_menu():
    # This function will print the menu for the main program
    print(30 * "-" , "VEHICLE MENU" , 30 * "-")
    print("1. View vehicle collection")
    print("2. Add new vehicle")
    print("3. Remove existing vehicle")
    print("4. Update vehicle information")
    print("--------------------------------------")
    print("After updating vehicle information: ")
    print("5. Calculate vehicle carbon footprint")
    print("6. Vehicle report")
    print(75 * "-")


def restart():
    # This function will ask the user to restart the program
    confirmation = input("Do you wish to perform another operation?(yes/y/no/n): ")

    if confirmation == "yes" or confirmation == "y":
        main()
    else:
        exit("See you soon for another operation!")


loop = True


def main():
    # This is the main program containing the work flow and all the functions and methods from the classes
    # Testing:
    # Scenario 1: The user will remove a vehicle which is out of the range or remove a car which has been removed?
    # Error 1: After I tried it, it shows us error that the index is out of range then the program crashes
    # Resolution 1: I fixed the issue by putting all the available vehicle before the user so he can remember which
    # car or moto is still available so that the user avoid the mistake
    # Scenario 2: After the information updates, are the information updated into the instance?
    # Error 2: There is no error, it is working properly and all the information are updated
    # Scenario 3: What if the user want to know the carbon footprint directly without updating the information?
    # Error 3: It will give an error "ZeroDivisionError: division by zero" because in the method there is a division
    # in order to get some values
    # Resolution 3: The better I can do to solve it is to tell the user to update the information before so that
    # the program doesn't crash
    # Scenario 4: What if the user want to have the report and the report shows no data or all the instances are 0?
    # Error 4: Yes, the game doesn't crash but the information are all 0 because no information has been updated
    # Resolution 4: The same as for the carbon footprint, I tell the user to update the vehicle information before
    # Scenario 5: What if the user insert string instead of int during information updates?
    # Error 5: Yes, it gets an error such as "invalid literal for int"
    # Resolution 5: In order to avoid the game crashing, I put the format needed before the user input any value
    while loop:
        print_menu()
        choice = int(input("Enter your choice [1-6]: "))

        if choice == 1:
            # View vehicle
            print("View vehicle collection has been selected")
            print("-------- Car collection --------")
            view_car()
            print("")
            print("-------- Moto collection --------")
            view_moto()
            restart()
        elif choice == 2:
            # Add vehicle
            print("Add new vehicle has been selected")

            true = True

            while true:
                print("------ Vehicle Type ------")
                print("1. Car")
                print("2. Moto")
                print("---------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    add_car()
                    restart()
                elif selection == 2:
                    add_moto()
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 3:
            # Remove vehicle
            print("Remove existing vehicle has been selected")

            true = True

            while true:
                print("------ Vehicle Type ------")
                print("1. Car")
                print("2. Moto")
                print("---------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    remove_car()
                    restart()
                elif selection == 2:
                    remove_moto()
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 4:
            # Update vehicle
            print("Update vehicle information has been selected")

            true = True

            while true:
                print("------ Vehicle Type ------")
                print("1. Car")
                print("2. Moto")
                print("---------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    index = 0
                    print("------ Car Collection ------ ")
                    for car in car_collection:
                        print(str(index) + ". " + car.model)
                        index += 1
                    selection = int(input("Enter car number [ex: 1]: "))
                    selected_car = car_collection[selection]
                    print("Selected car: " + selected_car.model)

                    revenue = selected_car.update_revenue()
                    rent_time = selected_car.update_rent_time()
                    miles = selected_car.update_miles()
                    gallons = selected_car.update_gallons()
                    carbon = selected_car.update_carbon()
                    print("Information updated successfully for " + selected_car.model)
                    print("--------------------------")
                    print(selected_car.info_details())
                    restart()
                elif selection == 2:
                    index = 0
                    print("------ Moto Collection ------ ")
                    for moto in moto_collection:
                        print(str(index) + ". " + moto.model)
                        index += 1
                    selection = int(input("Enter moto number [ex: 1]: "))
                    selected_moto = moto_collection[selection]
                    print("Selected moto: " + selected_moto.model)

                    helmet_number = selected_moto.update_helmet_number()
                    revenue = selected_moto.update_revenue()
                    rent_time = selected_moto.update_rent_time()
                    miles = selected_moto.update_miles()
                    gallons = selected_moto.update_gallons()
                    carbon = selected_moto.update_carbon()
                    print("Information updated successfully for " + selected_moto.model)
                    print("---------------------------")
                    print(selected_moto.info_details())
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 5:
            # Calculate vehicle carbon footprint
            print("Calculate vehicle carbon footprint has been selected")
            true = True

            while true:
                print("------ Vehicle Type ------")
                print("1. Car")
                print("2. Moto")
                print("---------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    index = 0
                    print("------ Car Collection ------ ")
                    for car in car_collection:
                        print(str(index) + ". " + car.model)
                        index += 1
                    selection = int(input("Enter car number [ex: 1]: "))
                    selected_car = car_collection[selection]
                    print("Selected car: " + selected_car.model)

                    result = selected_car.get_carbon_footprint()
                    print("The carbon footprint for  " + selected_car.model + " is " + str(result) + " tC02")
                    print("--------------------------")
                    restart()
                elif selection == 2:
                    index = 0
                    print("------ Moto Collection ------ ")
                    for moto in moto_collection:
                        print(str(index) + ". " + moto.model)
                        index += 1
                    selection = int(input("Enter moto number [ex: 1]: "))
                    selected_moto = moto_collection[selection]
                    print("Selected moto: " + selected_moto.model)

                    result = selected_moto.get_carbon_footprint()
                    print("The carbon footprint for  " + selected_moto.model + " is " + str(result) + " tC02")
                    print("--------------------------")
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        elif choice == 6:
            # Vehicle report
            print("Vehicle report has been selected")

            true = True

            while true:
                print("------ Vehicle Type ------")
                print("1. Car")
                print("2. Moto")
                print("---------------------------")
                selection = int(input("Enter your choice [1-2]: "))

                if selection == 1:
                    index = 0
                    print("------ Car Collection ------ ")
                    for car in car_collection:
                        print(str(index) + ". " + car.model)
                        index += 1
                    selection = int(input("Enter car number [ex: 1]: "))
                    selected_car = car_collection[selection]
                    print("Selected car: " + selected_car.model)

                    print(selected_car.report())
                    print("--------------------------")
                    restart()
                elif selection == 2:
                    index = 0
                    print("------ Moto Collection ------ ")
                    for moto in moto_collection:
                        print(str(index) + ". " + moto.model)
                        index += 1
                    selection = int(input("Enter moto number [ex: 1]: "))
                    selected_moto = moto_collection[selection]
                    print("Selected moto: " + selected_moto.model)

                    print(selected_moto.report)
                    print("--------------------------")
                    restart()
                else:
                    input("Wrong option selected. Enter any key to try again: ")
        else:
            input("Wrong option selection. Enter any key to try again: ")


main()




