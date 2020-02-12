# Name
print("Mahalinoro Razafimanjato" + "\n")

# This program will help Omondi to manage his car rental business
# He can view the initial cars, add new cars, remove cars, counting the money, and do multiple operation

# This is Omondi's car collection
# Using nested dictionaries instead of separate dictionaries for the car collection
car_collection = \
    {1: {"Model": "RAV4", "Year Released": 2015, "Year Acquired": 2013, "Rent Time": 20, "Plate Number": "1258 TAB"},
    2: {"Model": "Chevrolet", "Year Released": 2016, "Year Acquired": 2016, "Rent Time": 12, "Plate Number": "5836 TU"},
    3: {"Model": "Bus", "Year Released": 2017, "Year Acquired": 2017, "Rent Time": 10, "Plate Number": "4732 WWT"},
    4: {"Model": "Swift", "Year Released": 2017, "Year Acquired": 2017, "Rent Time": 15, "Plate Number": "1225 TAB"},
    5: {"Model": "Ferrari", "Year Released": 2018, "Year Acquired": 2017, "Rent Time": 16, "Plate Number": "5226 XTZ"},
    6: {}, 7: {}, 8: {}
     }

def view_car():
    # This function will display Omondi's car
    print("These are the car available:")
    for x, y in car_collection.items():
        print("\nCar ID:",x)
        for key in y:
            print(key + " : ", y[key])

def add_car():
    # This function will add cars to the collection
    print("Add the details of the new car:")
    range_number = int(input("Insert a number starting from 6: "))
    car_collection[range_number]["Model"] = input("What is the model of the car?: ")
    car_collection[range_number]["Year Released"] = int(input("When was it released?: "))
    car_collection[range_number]["Year Acquired"] = int(input("When was it acquired?: "))
    car_collection[range_number]["Rent Time"] = int(input("How many times has it been used?: "))
    car_collection[range_number]["Plate Number"] = input("What is the plate number?: ")
    print("The new car has been added successfully")

def remove_car():
    # This function will remove cars from the collection
    car_id = int(input("What is the car id that you want to remove?: "))
    car_collection.pop(car_id)
    print("The car number " + str(car_id) + " has been removed successfully")

money = 0
def count_money():
    # This function will count the money made from each car rented
    global money
    # Assuming that the rent for each car is the same
    revenue = int(input("What is the revenue for each car rent?: "))
    for x, y in car_collection.items():
        if y and "Rent Time" in y.keys():
            # This is the amount of money from the revenue of each car multiplied by the number of times it has been rented
            money += revenue * y["Rent Time"]

time = 0
def count_times_rent():
    # This function will count the number of times every car has been rented
    global time
    for x, y in car_collection.items():
        if y and "Rent Time" in y.keys():
            time += y["Rent Time"]

def car_operation_menu():
    # This function will allow Omondi to do multiple operations with his business
    # A combination of the different functions above (view, add, remove, and count)
    print("****************** CAR RENTAL MENU ******************")
    choice = int(input("""
        1: View all available car in the garage
        2: Add a new car in the business
        3: Remove a car from the business
        4: Count the revenue from each car
        5: Count the number of times each car has been rented
        Please enter your choice: """))
    if choice == 1:
        # This is the function that display all the cars and their characteristics
         view_car()
         restart = input("Do you wish to perform another operation? (yes/y/no/n): ")
         if restart == "yes" or restart == "y":
             car_operation_menu()
         else:
             exit()
    elif choice == 2:
        # This is the function that allow Omondi to add a new car to the list
         add_car()
         restart = input("Do you wish to perfom another operation? (yes/y/no/n): ")
         if restart == "yes" or restart == "y":
             car_operation_menu()
         else:
             exit()
    elif choice == 3:
        # This will allow Omonodi to remove a car form the list
         remove_car()
         restart = input("Do you wish to perform another operation? (yes/y/no/n): ")
         if restart == "yes" or restart == "y":
             car_operation_menu()
         else:
             exit()
    elif choice == 4:
        # This function will allow Omondi to count the total money he got from each car
        count_money()
        print("The total revenue of each car rented is " + str(money) + " RWF" + ".")
        restart = input("Do you wish to perform another operation? (yes/y/no/n): ")
        if restart == "yes" or restart == "y":
            car_operation_menu()
        else:
            exit()
    elif choice == 5:
        # This function will allow Omondi to see how many times the cars have been rented
        count_times_rent()
        print("The number of times each car has been rented is " + str(time) + ".")
        restart = input("Do you wish to perform another operation? (yes/y/no/n): ")
        if restart == "yes" or restart == "y":
            car_operation_menu()
        else:
            exit()
    else:
        # This is an error message in case Omondi input something else other than 1 to 5
        print("You can only choose between 1 and 5!")
        print("Please choose again!")
        car_operation_menu()

car_operation_menu()


