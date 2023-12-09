from extended_list import IntegerList

from unittest import TestCase, main


class TestExtendedList(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_constructor(self):
        self.assertEqual(self.list._IntegerList__data, [1, 2, 3, 4, 5])

    def test_add_successful(self):
        expected_list = self.list.get_data() + [420]

        output = self.list.add(420)
        self.assertEqual(expected_list, output)

    def test_add_raise_indexerror(self):
        with self.assertRaises(Exception) as ex:
            self.list.add('asd')

        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_remove_index(self):
        expected_output = self.list.get_data()[3]
        output = self.list.remove_index(3)
        self.assertEqual(expected_output, output)

    def test_remove_index_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.list.remove_index(len(self.list.get_data()))
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_constructor_values_not_integers(self):
        new_list = IntegerList(1, 2, 'a', 4.5, 5)
        self.assertEqual([1, 2, 5], new_list.get_data())

    def test_get_successful(self):
        expected_output = self.list.get_data()[3]
        output = self.list.get(3)
        self.assertEqual(expected_output, output)

    def test_get_index_error(self):
        with self.assertRaises(Exception) as ex:
            self.list.get(len(self.list.get_data()))

        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_successful(self):
        expected_output = self.list.get_data()
        expected_output.insert(2, 22)

        self.list.insert(2, 22)
        self.assertEqual(expected_output, self.list.get_data())

    def test_insert_raise_indexerror(self):
        index = len(self.list.get_data())

        with self.assertRaises(Exception) as ex:
            self.list.insert(index, 1)

        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_biggest(self):
        expected_result = max(self.list.get_data())

        self.assertEqual(expected_result, self.list.get_biggest())

    def test_get_index(self):
        self.assertEqual(2, self.list.get_index(3))


if __name__ == '__main__':
    main()
