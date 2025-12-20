#duck_typing

class Car:
    def move(self):
        print("Car is moving")

class Bike:
    def move(self):
        print("Bike is moving")

def start_vehicle(vehicle):
    vehicle.move()
start_vehicle(Car())
start_vehicle(Bike())

#Example 2
class Person:
    def name(self):
        print("vinayak is running")
class address:
    def name(self):
        print("Yellapura")
def show(details):
    details.name()
show(Person())
show(address())