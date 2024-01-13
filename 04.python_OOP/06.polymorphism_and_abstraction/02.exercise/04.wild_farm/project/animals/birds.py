from .animal import Bird
from ..food import Food, Meat


class Owl(Bird):
    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.25 * food.quantity
        super().feed(food)

    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)


class Hen(Bird):
    def make_sound(self):
        return 'Cluck'

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        super().feed(food)

    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

