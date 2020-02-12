# This is the test file for vehicle class
from vehicle_file import Vehicle

# Vehicle test instance
test_vehicle = Vehicle("Toyota", 2012, 2014, 0, "1212 TBA", 0)

# Method calls testing
print(test_vehicle.vehicle_info())
print(test_vehicle.update_revenue())
print(test_vehicle.update_rent_time())

# I get an error about int + str issue but I fixed it now and it works properly
print(test_vehicle.report())

# Every method calls in this test works perfectly fine now

