# This is the test file for moto class
from moto_class_file import Moto

# Moto instance for testing
test_moto = Moto("Yamaha", 2012, 2015, 0, "1212 TBA", 0, 0, 0, 0, 0, 0)

# Method calls testing
print(test_moto.info())
print(test_moto.info_details())
print(test_moto.update_helmet_number())
print(test_moto.update_miles())
print(test_moto.update_gallons())
print(test_moto.update_carbon())
print(test_moto.get_carbon_footprint())
print(test_moto.report())

# The methods call are working perfectly but in order to get the revenue and the rent times we have to call the vehicle
# instance in order for the information to be updated
