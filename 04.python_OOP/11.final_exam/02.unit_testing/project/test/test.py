from project.railway_station import RailwayStation
from collections import deque
from unittest import TestCase, main


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway_station = RailwayStation('testName')

    def test_init(self):
        self.assertEqual('testName', self.railway_station.name)
        self.assertEqual(deque(), self.railway_station.arrival_trains)
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_new_arrival_on_board(self):
        self.railway_station.new_arrival_on_board('testTrain')
        self.railway_station.new_arrival_on_board('someTrain')
        self.assertEqual(deque(['testTrain', 'someTrain']), self.railway_station.arrival_trains)

    def test_train_has_arrived_valid(self):
        train = 'testTrain123'
        self.railway_station.arrival_trains.append(train)
        self.railway_station.arrival_trains.append(train*2)
        msg = self.railway_station.train_has_arrived(train)
        self.assertEqual(msg, f'{train} is on the platform and will leave in 5 minutes.')
        self.assertEqual(deque(['testTrain123testTrain123']), self.railway_station.arrival_trains)
        self.assertEqual(deque(['testTrain123']), self.railway_station.departure_trains)

    def test_train_has_arrived_empty_arrival_trains(self):
        train = 'testTrain123'
        self.railway_station.arrival_trains.append(train)
        msg = self.railway_station.train_has_arrived(train)
        self.assertEqual(msg, f'{train} is on the platform and will leave in 5 minutes.')
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque(['testTrain123']), self.railway_station.departure_trains)

    def test_train_has_arrived_but_not_first(self):
        train = 'testTrain123'
        self.railway_station.arrival_trains.append('someTrain')
        self.railway_station.arrival_trains.append(train)
        msg = self.railway_station.train_has_arrived(train)
        self.assertEqual(f'There are other trains to arrive before {train}.', msg)
        self.assertEqual(deque(['someTrain', train]), self.railway_station.arrival_trains)

    def test_train_has_left_first(self):
        train = 'testTrain123'
        self.railway_station.departure_trains.append(train)
        self.assertTrue(self.railway_station.train_has_left(train))
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_train_has_left_not_first(self):
        train = 'testTrain123'
        self.railway_station.departure_trains.append('someTrain')
        self.railway_station.departure_trains.append(train)
        self.assertFalse(self.railway_station.train_has_left(train))
        self.assertEqual(deque(['someTrain', train]), self.railway_station.departure_trains)


if __name__ == '__main__':
    main()
