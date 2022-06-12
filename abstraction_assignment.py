#abstration example
from abc import ABC, abstractmethod

#abstract class
class Neighborhood(ABC):

    #regular method
    def size(self, amount):
        print("There are {} houses in this neighborhood.".format(str(amount)))
    
    #abstract method - implementation is not defined here
    @abstractmethod
    def maxSize(self, amount):
        pass

#child class
class House(Neighborhood):

    #This method defines the implementation of the abstract method from the parent class
    def maxSize(self, amount):
        print("Because there's already {} houses in the neighborhood, no more can be built.".format(str(amount)))

#instanciate the child class
obj = House()

#call the regular method
obj.size(32)

#call the abstract method
obj.maxSize(32)