from .animal import Mammal
from ..food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return 'Squeak'

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.1 * food.quantity
        super().feed(food)

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)


class Dog(Mammal):
    def make_sound(self):
        return 'Woof!'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.4 * food.quantity
        super().feed(food)

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)


class Cat(Mammal):
    def make_sound(self):
        return 'Meow'

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.3 * food.quantity
        super().feed(food)

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)


class Tiger(Mammal):
    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity
        super().feed(food)

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)
