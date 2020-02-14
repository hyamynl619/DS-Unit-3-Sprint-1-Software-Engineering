
"""
Define a Pet class with their attributes
"""




class Pet(object):
    

    def __init__(self, name, speaks):
   
       self.name = name
       self.speaks = speaks

    def full_name(self):
        return f"{self.name}"

   

    def speaks(self):
        print({self.name} + ' speaks')
        

if __name__ == "__main__":
    
    pet = Pet(name="Dog", speaks="Woof Woof")
    print(pet.full_name)
    




    

 


