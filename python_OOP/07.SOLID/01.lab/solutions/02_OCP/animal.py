from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Turtle(Animal):

    def make_sound(self):
        return '*turtle noises*'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

animals = [Cat(), Dog(), Turtle()]
animal_sound(animals)
