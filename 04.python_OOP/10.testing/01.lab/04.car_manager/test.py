from car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('BMW', 'E34', 7.1, 96)

    def test_init(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual('E34', self.car.model)
        self.assertEqual(7.1, self.car.fuel_consumption)
        self.assertEqual(96, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', 'E34', 7.1, 96)

        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_empty_model(self):
        with self.assertRaises(Exception) as ex:
            car = Car('BMW', '', 7.1, 96)

        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car('BMW', 'E34', -7.1, 96)

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            car = Car('BMW', 'E34', 0, 96)

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10

        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_zero_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_refuel_valid(self):
        added_fuel = 10
        expected_fuel = self.car.fuel_amount + added_fuel

        self.car.refuel(added_fuel)
        self.assertEqual(expected_fuel, self.car.fuel_amount)

    def test_refuel_invalid_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_too_large_expected_fuel_amount_equals_fuel_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 10)

        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_valid_input(self):
        distance = 10
        needed_fuel = (distance/100) * self.car.fuel_consumption
        self.car.fuel_amount = needed_fuel + 1

        self.car.drive(distance)

        self.assertEqual(1, self.car.fuel_amount)

    def test_drive_invalid_input(self):
        distance = 100
        needed_fuel = (distance / 100) * self.car.fuel_consumption
        self.car.fuel_amount = needed_fuel - 1

        with self.assertRaises(Exception) as ex:
            self.car.drive(distance)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_without_fuel_raises_exception(self):
        self.car.fuel_amount = 1

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
