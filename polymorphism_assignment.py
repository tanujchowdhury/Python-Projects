#parent class
class Merchandise:
    description = 'merchandise'
    price = 0

    #function 
    def getInfo(self):
        msg = 'This {} costs ${}.'.format(self.description, self.price)
        print(msg)

#child class
class Poster(Merchandise):
    description = 'poster'
    price = 15
    subject = 'Star Wars'
    area = '11x17 inch'

    #polymorphism
    def getInfo(self):
        msg = 'This {} {} {} costs ${}.'.format(self.area, self.subject, self.description, self.price)
        print(msg)

#child class
class Hoodie(Merchandise):
    description = 'hoodie'
    price = 25
    color = 'red'
    size = 'medium'

    #polymorphism
    def getInfo(self):
        msg = 'This {} {} {} costs ${}.'.format(self.size, self.color, self.description, self.price)
        print(msg)

thing1 = Merchandise()
thing1.getInfo()

poster1 = Poster()
poster1.getInfo()

hoodie1 = Hoodie()
hoodie1.getInfo()