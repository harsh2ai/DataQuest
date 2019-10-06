# Python program to illustrate OOP concepts

# to explain structure of a class
# Base class with 2 property

class Vehicle:
    # constructor used to initialize the object
    # value set for one property and default value applied for other
    def __init__(self, num_of_tyres):
        self.tyre_count = num_of_tyres
        self.primary_color = "unknown"
    # methods to set object property
    def inputColor(self, color):
        self.primary_color = color
    # method to show the properties of vehicle.
    def dispDetails(self):
        print("Number of tyres: ", self.tyre_count, "Color of Vehicle: ", self.primary_color)

# subclass which inherits base class methods and property
class MotorCycle(Vehicle):
    def __init__(self, num_of_tyres, color):
        Vehicle.__init__(self,num_of_tyres)
        Vehicle.inputColor(self,color)

# main code
# create objects for base class and subclass to verify if properties are shown
v = Vehicle(4)
v.dispDetails()
m = MotorCycle(2, "Red")
m.dispDetails()
# to show that base object can be used to reference subclass objects
v = m
m.dispDetails()