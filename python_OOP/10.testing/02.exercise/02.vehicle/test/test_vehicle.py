from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 168)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(168, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_valid_input(self):
        fuel_needed = 95.5
        kilometres = fuel_needed / self.vehicle.fuel_consumption

        self.vehicle.drive(kilometres)

        self.assertEqual(4.5, self.vehicle.fuel)

    def test_drive_invalid_input(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_valid_input(self):
        self.vehicle.fuel -= 20

        self.vehicle.refuel(18)

        self.assertEqual(98, self.vehicle.fuel)

    def test_refuel_invalid_input(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual('Too much fuel', str(ex.exception))

        self.vehicle.fuel -= 1
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(2)

        self.assertEqual('Too much fuel', str(exc.exception))

    def test_str(self):
        self.assertEqual((f"The vehicle has 168 "
                          f"horse power with 100 fuel left and {self.vehicle.fuel_consumption} fuel consumption"),
                         str(self.vehicle))


if __name__ == '__main__':
    main()
