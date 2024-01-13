class Flower:
    def __init__(self,name:str,water_requirements:int):
        self.name = name
        self.water_requirements = water_requirements
    
    is_happy = False
    
    def water(self, quantity):
        if quantity>=self.water_requirements:
            self.is_happy=True
    
    def status(self):
        return f'{self.name} is{" not" if not self.is_happy else ""} happy'