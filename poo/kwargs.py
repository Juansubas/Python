def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")
        
show(name = "Hector", country = "Mexico", age = 30)