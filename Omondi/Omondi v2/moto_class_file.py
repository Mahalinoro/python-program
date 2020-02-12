# This is the file containing the moto class
# importing the Vehicle class
# importing numpy to perform mathematic calculation
from vehicle_file import Vehicle
import numpy as np


# This is the moto class
class Moto(Vehicle):
    # This is the method __init__ that will create instances automatically
    def __init__(self, model, year_released, year_acquired, rent_time, plate_number, revenue, helmet_number, miles,
                 gallons, carbon, carbon_footprint):
        super().__init__(model, year_released, year_acquired, rent_time, plate_number, revenue)
        self.helmet_number = helmet_number
        self.miles = miles
        self.gallons = gallons
        self.carbon = carbon
        self.carbon_footprint = carbon_footprint

    def info(self):
        # This method will display the information about model and plate number for the moto
        return self.model + " - " + "Plate Number: " + self.plate_number

    def info_details(self):
        # This method will display detailed information about the moto
        return "Moto Model: " + self.model + "\n" + "Revenue: " + str(
            self.revenue) + "\n" + "Yearly Miles: " + str(
            self.miles) + "\n" + "Gallons consumed: " + str(self.gallons) + "\n" + \
               "Carbon emmited: " + str(self.carbon) \
               + "\n" + "Helmets Available: " + str(self.helmet_number) + "\n"

    def update_helmet_number(self):
        # This method will ask the user the number of available helmet and update the information to the instance
        number_helmet = int(input("Insert the number of helmet available: "))
        self.helmet_number = number_helmet + self.helmet_number
        return self.helmet_number

    def update_miles(self):
        # This method will ask the user the miles made yearly and will update the information
        self.miles = int(input("Insert the miles made yearly [number]: "))
        return self.miles

    def update_gallons(self):
        # This method will ask the user the gallons consumed
        self.gallons = int(input("Insert the gallons volume consumed [number]: "))
        return self.gallons

    def update_carbon(self):
        # This method will ask the user the carbon emitted
        self.carbon = int(input("Insert the grams of CO2 emitted [number]: "))
        return self.carbon

    def get_carbon_footprint(self):
        # This method will calculate the carbon footprint of a moto
        # First, getting the number of year released
        # Then, the average mile made yearly
        # After, the gallons per mile made
        # Last, the carbon per gallon made
        # With the formula of carbon footprint, we get the value of the carbon footprint
        number_year_released = 2019 - self.year_released
        average_mile = np.mean(self.miles)
        gallons_mile = self.gallons / self.miles
        carbon_gallon = self.carbon / self.gallons
        self.carbon_footprint = round(number_year_released * (10000 * average_mile) *
                                      (2 * gallons_mile) * (9 * carbon_gallon))
        return self.carbon_footprint

    def report(self):
        # This method will give the user the report about the revenue, number of times the moto has been rented and
        # the carbon footprint
        return "Revenue: " + str(self.revenue) + "\n" + "Number of rented times: " + str(self.rent_time) + \
               "\n" + "Carbon Footprint: " + str(self.carbon_footprint)
