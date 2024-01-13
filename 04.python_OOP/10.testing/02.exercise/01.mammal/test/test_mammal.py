# marked 01.mammal as sources root
from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Catto', 'Cat', 'Meow')

    def test_init(self):
        self.assertEqual(self.mammal.name, 'Catto')
        self.assertEqual(self.mammal.type, 'Cat')
        self.assertEqual(self.mammal.sound, 'Meow')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        self.assertEqual('Catto makes Meow', self.mammal.make_sound())
        self.mammal.name = 'Doggo'
        self.mammal.sound = 'Woof'
        self.assertEqual('Doggo makes Woof', self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('Catto is of type Cat', self.mammal.info())
        self.assertEqual('Doge is of type dog', Mammal('Doge', 'dog', 'Woof').info())


if __name__ == '__main__':
    main()
