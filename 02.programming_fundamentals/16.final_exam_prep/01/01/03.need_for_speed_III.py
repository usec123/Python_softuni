MAX_TANK_CAPACITY = 75

class Car:
    def __init__(self,name,mileage,fuel):
        self._name = name
        self._mileage = mileage
        self._fuel = fuel
    
    def drive(self,distance,fuel):
        if self._fuel < fuel:
            print('Not enough fuel to make that ride')
        else:
            self._mileage+=distance
            self._fuel-=fuel
            print(f'{self._name} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if self._mileage >= 100_000:
                print(f'Time to sell the {self._name}!')
                cars.remove(self)
    
    def refuel(self,fuel):
        free_space = MAX_TANK_CAPACITY-self._fuel
        if free_space >= fuel:
            self._fuel+=fuel
            print(f'{self._name} refueled with {fuel} liters')
        else:
            diff = MAX_TANK_CAPACITY-self._fuel
            self._fuel = MAX_TANK_CAPACITY
            print(f'{self._name} refueled with {diff} liters')
    
    def revert(self,distance):
        self._mileage-=distance
        if self._mileage<10_000:
            self._mileage = 10_000
        else:
            print(f'{self._name} mileage decreased by {distance} kilometers')
    
    def __repr__(self):
        return self._name

    def info(self):
        return f'{self._name} -> Mileage: {self._mileage} kms, Fuel in the tank: {self._fuel} lt.'

n = int(input())

cars = []

for _ in range(n):
    info = input().split('|')
    cars.append(Car(info[0],int(info[1]),int(info[2])))

cmd = input()
while cmd!='Stop':
    cmd = cmd.split(' : ')
    
    if cmd[0] == 'Drive':
        car = cmd[1]
        distance = int(cmd[2])
        fuel = int(cmd[3])
        index = [current_car._name for current_car in cars].index(car)
        cars[index].drive(distance,fuel)
    
    elif cmd[0]=='Refuel':
        car = cmd[1]
        fuel = int(cmd[2])
        index = [current_car._name for current_car in cars].index(car)
        cars[index].refuel(fuel)
    
    elif cmd[0]=='Revert':
        car = cmd[1]
        kilometers = int(cmd[2])
        index = [current_car._name for current_car in cars].index(car)
        cars[index].revert(kilometers)

    cmd = input()
    
for car in cars:
    print(car.info())