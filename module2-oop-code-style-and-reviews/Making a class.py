
"""
Define a Pet class with their attributes
"""

class Pet(object):
    eats = 'food'

    def __init__(self, name):
        self.name = name

    def speaks(self):
        print(self.name + ' speaks')
    
    def eat(self, meal):
        if meal == self.eats:
            print('Bark!')
        else:
            print('GRR!')


my_pet = Pet('Dog')

my_pet.speak()
my_pet.eat('food')
   
