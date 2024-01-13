from worker import Worker
from unittest import TestCase, main


class WorkerTests(TestCase):

    # without setup => make a new instance in every test
    # with setup => def a setup method

    def setUp(self):
        self.worker = Worker('TestGuy', 25000, 100)

    # test name methods should start with test_
    def test_correct_initialization(self):
        # Arrange & Act
        # self.worker = Worker('TestGuy', 25000, 100)

        # Assert
        self.assertEqual('TestGuy', self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_energy(self):
        expected_money = self.worker.money + self.worker.salary
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_without_energy_expected_exception(self):
        self.worker.energy = 0  # Arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # Act

        self.assertEqual('Not enough energy.', str(ex.exception))  # Assert

    def test_increment_energy_on_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()
