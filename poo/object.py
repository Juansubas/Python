class People:
    classname = 'Juansubas'
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age
        
    def hi(self ):
        print("Hi " + self.name)
        
    def get_age(self):
        return self.__age
    
    def __some(self):
        print("Some")
        
    @staticmethod
    def helloworld():
        print("Hello World")
    
    @classmethod
    def helloworld2(cls):
        print("Hello World2")
    
  
juan = People("Juan", 20)

juan.hi()

juan.helloworld()

People.helloworld2()

print(juan.get_age())

# Method Private not works juan.__some

#Same constructor using pass
class Barman(People):
    pass

    def welcome(self):
        print("Welcome")

juan = Barman("Juan", 20)
juan.welcome()