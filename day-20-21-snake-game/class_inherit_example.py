class Animal:
    def __init__(self):
        number_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale")
        

class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print("Swimming...")
        
    def breathe(self):
        super().breathe()
        print("We are using our gills.")
        

rex = Animal()
tim = Fish()
rex.breathe()
tim.breathe()
tim.swim()