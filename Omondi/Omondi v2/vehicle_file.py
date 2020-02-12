# This is the file containing the Vehicle class parent
class Vehicle:
    # The __init__ method to create a vehicle instance automatically
    def __init__(self, model, year_released, year_acquired, rent_time, plate_number, revenue):
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.rent_time = rent_time
        self.plate_number = plate_number
        self.revenue = revenue

    def vehicle_info(self):
        # This method will display the vehicle information
        return "Vehicle Model: " + self.model + "\n" + "Year Acquired: " + str(
            self.year_acquired) + "\n" + "Year Released: " + str(
            self.year_released) + "\n" + "Plate Number: " + self.plate_number + "\n"

    def update_revenue(self):
        # This method will update the revenue by user input
        amount = int(input("Insert the revenue [number]: "))
        self.revenue = amount + self.revenue
        return self.revenue

    def update_rent_time(self):
        # This method will update the rent time by user input
        number_time = int(input("Insert number of times it has been rented: "))
        self.rent_time = number_time + self.rent_time
        return self.rent_time

    def report(self):
        # This method will display the report for revenue and rent_time
        return "Revenue: " + str(self.revenue) + "\n" + "Number of rented times: " + str(self.rent_time)
