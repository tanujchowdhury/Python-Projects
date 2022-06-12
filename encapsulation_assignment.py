#Encapsulation example - implemented by creating a protected or private method or attribute

class Capsule:
    def __init__(self):

        #Define a protected attribute with _
        self._protectedVar = 15

        #Define a private attribute with__
        self.__privateVar = 37
    
    #Method to print private variable
    def getPrivate(self):
        print(self.__privateVar)

    


#Instanciate the class
obj = Capsule()

#Protected var can be accessed this way, but not provite vars
print(obj._protectedVar)

#This code returns an AttributeError if run
#print(obj.__privateVar)

#This code prints the private var
obj.getPrivate()