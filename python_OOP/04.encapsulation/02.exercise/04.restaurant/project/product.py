class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price
