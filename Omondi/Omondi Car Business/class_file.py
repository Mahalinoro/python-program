class Car:
    # This is the class file for the program
    def __init__(self, model, year_released, year_acquired, rent_time, plate_number, revenue):
        # This method will execute automatically and add all instances of class in the blueprint
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.rent_time = rent_time
        self.plate_number = plate_number
        self.revenue = revenue

    def info(self):
        # This method will display all the information of each car
        return "Car Model: " + self.model + "\n" + "Year Acquired: " + str(
            self.year_acquired) + "\n" + "Year Released: " + str(
            self.year_released) + "\n" + "Plate Number: " + self.plate_number + "\n" + "Rent time: " + \
            str(self.rent_time) + "\n" + "Revenue: " + str(self.revenue) + "\n"


    def get_revenue(self):
        # This method will ask Omondi the amount of money made by the car rent
        self.revenue = int(input("Enter the amount get from the selected car: "))
        return self.revenue

    def get_report(self):
        # This method is calling the revenue and rent time of a specific car
        return "Car Model: " + self.model + "\n" + "Revenue: " + str(self.revenue) + "\n" + "Rent Time: " + \
               str(self.rent_time)

    def get_rent_time(self):
        # This method will display the number of time a car has been rented
        # It will ask Omondi the number of times the car has been rented
        self.rent_time = int(input("Enter the number of times the selected car has been rented: "))
        return self.rent_time


