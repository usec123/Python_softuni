'''
class names use CamelCase
__init__ = dunder method (double under); acts like a constructor
self - used to transfer data in class (like fields)
'''

class Car:
    
    def __init__(self, make:str, model:str, year:int=0):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f'The {self.make} {self.model}\'s engine is starting')
        
    def drive(self,distance):
        print(f'The {self.make} {self.model} is driving {distance} kilometers')
        
    def stop_engine(self):
        print(f'The {self.make} {self.model}\'s engine is stopping')
        
car1 = Car('Toyota','Corolla',2020)
car2 = Car('Mercedes','S500')

print(car1.make)
print(car2.year)
car1.start_engine()
car2.start_engine()
car1.drive(200)
car2.drive(200)
car2.stop_engine()