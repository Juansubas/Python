class People:
  def __init__(self, name: str):
      self.name = name
    
  def hi(self ):
      print("Hola " + self.name)
  
hector = People("Juan")

hector.hi()

