class People:
    classname = 'Juansubas'
    
    def __init__(self, name: str):
        self.name = name
        
    def hi(self ):
        print("Hola " + self.name)
        
    @staticmethod
    def helloworld():
        print("Hello World")
    
    @classmethod
    def helloworld2(cls):
        print("Hola mundo2")
    
  
juan = People("Juan")

juan.hi()

juan.helloworld()

People.helloworld2()
