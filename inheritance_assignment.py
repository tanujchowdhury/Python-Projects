#Creating a parent class for vehicles
class Vehicle:

    #Define the attributes of the class
    make = ''
    model = ''
    color = ''


#Creating a child class for personal vehicles
class Family(Vehicle):
    trunk_size = 0
    seats = 4

#Creating a child class for company cars
class Company(Vehicle):
    current_driver = ''
    hours_driven = 0