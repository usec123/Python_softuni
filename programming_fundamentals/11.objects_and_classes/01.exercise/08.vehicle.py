class Vehicle:
    owner = None
    
    def __init__(self,type,model,price):
        self.type = type
        self.model = model
        self.price = price
        
    def buy(self, money, owner):
        if money >= self.price and self.owner == None:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money-self.price:.2f}'
        elif money < self.price:
            return 'Sorry, not enough money'
        else:
            return 'Car already sold'
    
    def sell(self):
        if self.owner != None: self.owner = None
        else: return 'Vehicle has no owner'
    
    def __repr__(self):
        return f'{self.model} {self.type} is owned by: {self.owner}'\
            if self.owner != None else\
                f'{self.model} {self.type} is on sale: {self.price}'
            
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, 
model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
