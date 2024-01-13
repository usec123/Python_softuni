class Cup:
    def __init__(self,size:int,quantity:int):
        self.size = size
        self.quantity = quantity
        
    def fill(self,quantity):
        if quantity <= self.size - self.quantity:
            self.quantity += quantity
        
    def status(self):
        return self.size - self.quantity