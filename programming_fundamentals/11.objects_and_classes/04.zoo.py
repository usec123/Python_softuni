class Zoo:
    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.__animals = 0
    
    def add_animal(self,species,name):
        if species == 'mammal':
            self.mammals.append(name)
            self.__animals += 1
        elif species == 'fish':
            self.fishes.append(name)
            self.__animals += 1
        else:
            self.birds.append(name)
            self.__animals += 1
    
    def get_info(self, species:str):
        if species == 'mammal':
            species = 'Mammals'
            animals = ', '.join(self.mammals)
        elif species == 'fish':
            species = 'Fishes'
            animals = ', '.join(self.fishes)
        else:
            species = 'Birds'
            animals = ', '.join(self.birds)
        return f'{species} in {self.name}: {animals}\nTotal animals: {self.__animals}'

name = input()
n = int(input())
zoo = Zoo(name)

for _ in range(n):
    cmd = input().split()
    zoo.add_animal(cmd[0],cmd[1])

print(zoo.get_info(input()))