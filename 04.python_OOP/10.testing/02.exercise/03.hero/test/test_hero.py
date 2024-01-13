from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('SomeSuperHero123', 4, 100, 25)

    def test_init(self):
        self.assertEqual('SomeSuperHero123', self.hero.username)
        self.assertEqual(420, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(200, self.hero.damage)

    def test_battle_valid_input(self):
        enemy_hero = Hero('Moon Lord', 5, 100, 15)
        self.assertEqual('You win', self.hero.battle(enemy_hero))
        self.assertEqual(5, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(30, self.hero.damage)

        enemy_hero.health = self.hero.health
        enemy_hero.damage = self.hero.damage
        enemy_hero.level = self.hero.level
        self.assertEqual('Draw', self.hero.battle(enemy_hero))
        self.assertEqual(-120, self.hero.health)

        self.hero.health = 1

        enemy_hero.health = 160
        enemy_hero.damage = 100
        self.assertEqual('You lose', self.hero.battle(enemy_hero))
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(15, enemy_hero.health)
        self.assertEqual(105, enemy_hero.damage)

    def test_battle_invalid_input(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

        self.hero.health = 0
        opponent = Hero('Plantera', 5, 100, 15)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(opponent)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        self.hero.health = 100
        opponent.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(opponent)

        self.assertEqual(f"You cannot fight {opponent.username}. He needs to rest", str(ex.exception))

    def test_str(self):
        self.assertEqual(("Hero SomeSuperHero123: 4 lvl\n"
                          "Health: 100\n"
                          "Damage: 25\n"),
                         str(self.hero))


if __name__ == '__main__':
    main()
