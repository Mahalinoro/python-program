from class_file import Car

# This is the function file for the program

# This is going to be the car collection and will be considered as instances
car_one = Car("RAV4", 2015, 2013, 0, "1258 TAB", 0)
car_two = Car("Chevrolet", 2016, 2016, 0, "5836 TU", 0)
car_three = Car("Bus", 2017, 2017, 0, "4732 WWT", 0)
car_four = Car("Swift", 2017, 2017, 0, "1225 TAB", 0)
car_five = Car("Ferrari", 2018, 2017, 0, "5226 XTZ", 0)

# Putting all the objects into a list for better manipulation
car_collection = [car_one, car_two, car_three, car_four, car_five]


def view_car():
    # This function will display all the car in the list
    index = 0
    for car_number in car_collection:
        print(str(index) + ". " + car_number.info())
        index += 1


def add():
    # This function will ask Omondi to add a new car in the collection
    model = input("What is the car model?: ")
    year_released = int(input("Which year was it released? [YYYY]: "))
    year_acquired = int(input("Which year was it acquired? [YYYY]: "))
    rent_time = int(input("How many times has it been rented?: "))
    plate_number = input("What is the plate number?: ")
    revenue = int(input("How much is the revenue made from it?: "))
    car_six = Car(model, year_released, year_acquired, rent_time, plate_number, revenue)
    car_collection.append(car_six)
    print("\n")
    print(car_six.model + " added successfully!")
    print(car_six.info())

def remove():
    # This function will ask Omondi to remove a car from the list
    index = 0
    for x in car_collection:
        print(str(index) + ". " + x.model)
        index += 1
    index = int(input("The car number you wish to remove [ex: 1]: "))
    selected_car = car_collection[index]
    confirmation = input("Are you sure you want to remove " + selected_car.model + "? [yes/y/no] :")
    if confirmation == "yes" or confirmation == "y":
        removed_car = car_collection.pop(index)
        print(removed_car.model + " removed successfully!")
    else:
        restart()


def car_operation():
    # This function is the main program which combine all the functions and class properties
    print("------------------------- CAR BUSINESS OPERATION -----------------------")
    choice = int(input("""
            1: View all available car
            2: Add a new car 
            3: Remove a car 
            4: Rent a car
            5: Add car rent times
            6: Report
            Please enter your choice: """))
    print("\n" + "-------------------------------------------------------------------------" + "\n")
    if choice == 1:
        view_car()
        restart()
    elif choice == 2:
        add()
        restart()
    elif choice == 3:
        print("Car collection: ")
        remove()
        restart()
    elif choice == 4:
        index = 0
        print("Car collection: ")
        for x in car_collection:
            print(str(index) + ". " + x.model)
            index += 1
        selection = int(input("Enter car number to be rented [ex: 1]: "))
        selected_car = car_collection[selection]
        print("Selected car: " + selected_car.model)

        result = selected_car.get_revenue()
        print("The revenue for the " + selected_car.model + " is $" + str(result) + ".")
        restart()
    elif choice == 5:
        index = 0
        print("Car collection: ")
        for x in car_collection:
            print(str(index) + ". " + x.model)
            index += 1
        selection = int(input("Enter car number [ex: 2]: "))
        selected_car = car_collection[selection]
        print("Selected car: " + selected_car.model)

        result = selected_car.get_rent_time()
        print("The number of times the " + selected_car.model + " has been rented is " + str(result) + ".")
        restart()
    elif choice == 6:
        index = 0
        print("Car collection: ")
        for x in car_collection:
            print(str(index) + ". " + x.model)
            index += 1
        selection = int(input("Enter car number [ex: 3] : "))
        selected_car = car_collection[selection]
        print(selected_car.get_report())
        restart()
    else:
        print("You can only choose between 1 to 5!")
        print("Please choose again: ")
        car_operation()


def restart():
    # This function is used to restart the program all over again if Omondi wish to do more than one operation
    restart = input("Do you wish to perform another operation?(yes/y/no/n): ")
    if restart == "yes" or restart == "y":
        car_operation()
    else:
        exit("See you soon for another operation!")
