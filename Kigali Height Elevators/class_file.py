# Importing random module - it will help us get random values for our variables
# Importing time for elevator display floor number
import random
import time


# For this program, we need 3 classes: Building, Elevator, and User
class Building:
    # Building will take attributes such as floor number, elevator and user
    def __init__(self):
        # Initializing the floor number, the elevator instance and user instance automatically
        self.numb_floor = 8
        self.elevator = Elevator()
        self.user = User(current_floor="", destination_floor="")

    def run(self):
        # Instance method that will run the main program
        # This function will display the info status of the elevator whether it is closed or open
        # It will print the current floor of the user and the elevator
        # The user will input the value number of his/her current floor
        # By using while loop, the elevator will come to the user current floor
        # Then, after it will take the user to the selected destination
        # This method as well will move the elevator depending on the user and elevator's floor
        self.elevator.status_info()
        user_floor = int(input("Which floor number are you? [0 - 8]: "))
        self.user.current_floor = user_floor
        if 0 <= user_floor <= 8:
            print("You are in floor number: " + str(self.user.current_floor))
            print("The elevator is in floor number: " + str(self.elevator.current_floor) + "\n")
            selection = int(input("Which floor number are you going?[0 - 8]: "))
            self.user.destination_floor = selection
            if 0 <= selection <= 8:
                while self.elevator.current_floor <= self.user.current_floor:
                    self.elevator.move_up()
                    if self.elevator.current_floor == self.user.current_floor:
                        time.sleep(1)
                        print("Elevator status: Open! You can enter.")
                        print("< ------------------------------------- >")
                        time.sleep(1)
                        print("Elevator status: Closed!")
                        print("> ------------------------------------- <")
                        break
                else:
                    while self.elevator.current_floor >= self.user.current_floor:
                        self.elevator.move_down()
                        if self.elevator.current_floor == self.user.current_floor:
                            time.sleep(1)
                            print("Elevator status: Open! You can enter.")
                            print("< ------------------------------------- >")
                            time.sleep(1)
                            print("Elevator status: Closed!")
                            print("> ------------------------------------- <")
                            break
                while self.elevator.current_floor <= self.user.destination_floor:
                    self.elevator.move_up()
                    if self.elevator.current_floor == self.user.destination_floor:
                        time.sleep(2)
                        print("Elevator status: Open!")
                        print("< ------------------------------------------- >")
                        print("You arrived at your destination!")
                        break
                else:
                    while self.elevator.current_floor >= self.user.destination_floor:
                        self.elevator.move_down()
                        if self.elevator.current_floor == self.user.destination_floor:
                            time.sleep(2)
                            print("Elevator status: Open!")
                            print("< ----------------------------------------- >")
                            print("You arrived at your destination!")
                            break
            else:
                print("Please, we only have 8 floors!")
                print("Try again!")
                self.run()
        else:
            print("Please, specify your correct location!")
            self.run()

class Elevator:
    # This class is specifically for the elevator and its attributes
    def __init__(self):
        self.direction = 1
        self.status = random.randint(0, 1)
        self.current_floor = random.randint(0, 8)

    def move_up(self):
        # This is about moving the elevator up by one floor
        self.current_floor += self.direction
        time.sleep(1)
        print("The elevator is moving up!")
        time.sleep(2)
        print("The elevator is now in floor number: " + str(self.current_floor))

    def move_down(self):
        # This is about moving the elevator down by one floor
        self.current_floor -= self.direction
        time.sleep(1)
        print("The elevator is moving down!")
        time.sleep(2)
        print("The elevator is now in floor number: " + str(self.current_floor))

    def status_info(self):
        # This will display if the elevator is open or closed
        if self.status == 0:
            print("Elevator status: Closed!")
            print("> ------------------------ <")
        else:
            print("Elevator status: Open!")
            print("< ------------------------ >")


class User:
    # This is the user class and its attributes
    def __init__(self, current_floor, destination_floor):
        self.current_floor = current_floor
        self.destination_floor = destination_floor
