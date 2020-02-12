# This is the car class test file
from car_class_file import Car

# I created a car test instance to try the different methods
test_car = Car("Yaris", 2014, 2015, 0, "1212 XYZ", 0, 0, 0, 0, 0)

# This are the method calls of the methods in the car class
print("info method test:")
print(test_car.info())
print("info_details method test:")
print(test_car.info_details())
print("update_miles, update_gallons, update_carbon methods test:")
print(test_car.update_miles())
print(test_car.update_gallons())
print(test_car.update_carbon())
print("carbon footprint method test:")
print(test_car.get_carbon_footprint())

# After testing the methods one by one, they are working perfectly as intended
