class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, topping_type):
        if topping_type:
            self.__topping_type = topping_type
        else:
            raise ValueError('The topping type cannot be an empty string')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('The weight cannot be less or equal to zero')

