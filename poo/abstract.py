from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def get_quantity():
      pass
    
    def descrption(self):
        print("Soy una bebida")
    
    
class Beer(Drink):
    def __init__(self, quantity):
        self.__quantity = quantity
        
    def get_quantity(self):
        return self.__quantity
        
beer = Beer(15)
print(beer.get_quantity())
beer.descrption()