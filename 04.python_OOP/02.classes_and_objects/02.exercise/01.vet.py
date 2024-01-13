class Vet:
    animals = []
    space = 5
    
    def __init__(self,name):
        self.name = name
        self.animals = []
        
    def register_animal(self, animal_name):
        if self.space > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            self.space -= 1
            return f'{animal_name} registered in the clinic'
        return 'Not enough space'

    def unregister_animal(self,animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f'{animal_name} unregistered successfully'
        return f'{animal_name} not in the clinic'

    def info(self):
        return f"{self.name} has {self.animals} animals. {Vet.space - self.animals} space left in clinic"