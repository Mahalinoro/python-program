# This is the file containing the car class
from vehicle_file import Vehicle
import numpy as np

# This is the car class
class Car(Vehicle):
    # This is the __init__ method which will create a car automatically
    def __init__(self, model, year_released, year_acquired, rent_time, plate_number, revenue, miles,
                 gallons, carbon, carbon_footprint):
        super().__init__(model, year_released, year_acquired, rent_time, plate_number, revenue)
        self.miles = miles
        self.gallons = gallons
        self.carbon = carbon
        self.carbon_footprint = carbon_footprint

    def info(self):
        # This method will display the model and plate number of the car
        return self.model + " - " + "Plate Number: " + self.plate_number

    def info_details(self):
        # This method will display the other information of the car such as the revenue, model, miles, carbon...
        return "Car Model: " + self.model + "\n" + "Revenue: " + str(
            self.revenue) + "\n" + "Yearly Miles: " + str(
            self.miles) + "\n" + "Gallons consumed: " + str(self.gallons) + "\n" + \
               "Carbon emitted: " + str(self.carbon) + "\n"

    def update_miles(self):
        # This method will ask the miles made yearly and update the information about the instance
        self.miles = int(input("Insert the miles made yearly [number]: "))
        return self.miles

    def update_gallons(self):
        # This method will ask the gallons consumed yearly and update the information about the instance
        self.gallons = int(input("Insert the gallons volume consumed [number]: "))
        return self.gallons

    def update_carbon(self):
        # This method will ask the carbon emitted yearly and update the information about the instance
        self.carbon = int(input("Insert the grams of CO2 emitted [number]: "))
        return self.carbon

    def get_carbon_footprint(self):
        # This method will calculate the carbon footprint of a specific car
        # First, getting the number of year released
        number_year_released = 2019 - self.year_released
        # Second, getting the average miles made yearly
        average_mile = np.mean(self.miles)
        # Third, getting the gallons per miles
        gallons_mile = self.gallons / self.miles
        # Fourth, getting the carbons per gallons
        carbon_gallon = self.carbon / self.gallons
        # Filth, using the carbon footprint formula to get the carbon footprint
        self.carbon_footprint = round(number_year_released * (12000 * average_mile) *
                                      (15 * gallons_mile) * (9 * carbon_gallon))
        return self.carbon_footprint

    def report(self):
        # This method will report the revenue, number of times the car has been rented, the carbon footprint
        return "Revenue: " + str(self.revenue) + "\n" + "Number of rented times: " + str(self.rent_time) + \
               "\n" + "Carbon Footprint: " + str(self.carbon_footprint)
