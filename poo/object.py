class People:
    classname = 'Juansubas'
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age
        
    def hi(self ):
        print("Hola " + self.name)
        
    def get_age(self):
        return self.__Age
        
    @staticmethod
    def helloworld():
        print("Hello World")
    
    @classmethod
    def helloworld2(cls):
        print("Hola mundo2")
    
  
juan = People("Juan", 20)

juan.hi()

juan.helloworld()

People.helloworld2()

print(juan.get_age())