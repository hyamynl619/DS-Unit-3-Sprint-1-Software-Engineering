
"""
Define a Pet class with their attributes
"""

   """
    Setting up the class attribute, same for all instances
    """


class Pet(object):
    eats = 'food'

    def __init__(self, name):
    """
    Define the init method
    """
       self.name = name

    """
    Instance Attribute, different for each instance
    """

    def speaks(self):
        print(self.name + ' speaks')

    """
    Define a method for speaking behavior
    """

    def eat(self, meal):
    """
    Define a method for eating behavior
    """
       if meal == self.eats:
            print('Bark!')
        else:
            print('GRR!')

    """
    Create an instance of Class
    """

my_pet = Pet('Dog')
   """
    Calling the method on the new instance
    """
my_pet.speak()
my_pet.eat('food')
