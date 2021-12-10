import unittest
from lib.recursor import Recursor

class TestRecursor(unittest.TestCase):
    def setUp(self):
        self.recursor = Recursor()
        # print("\n")
        # self.recursor.countdown(3)

    def test_get_sum(self):
        self.expected = 10
        self.actual = self.recursor.get_sum([1, 2, 3, 4])
        self.assertEqual(self.actual, self.expected)

    def test_factorial(self):
        self.expected = 120
        self.actual = self.recursor.factorial(5)
        self.assertEqual(self.actual, self.expected)

    def test_reverse_string(self):
        self.expected_1 = 'leirA'
        self.expected_2 = ''
        self.actual_1 = self.recursor.reverse_string('Ariel')
        self.actual_2 = self.recursor.reverse_string('')
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)

    def test_power(self):
        self.expected_1 = 16
        self.expected_2 = 32768
        self.actual_1 = self.recursor.power(2, 4)
        self.actual_2 = self.recursor.power(8, 5)
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)

    def test_is_palindrome(self):
        self.expected_1 = True
        self.expected_2 = True
        self.expected_3 = True
        self.expected_4 = False
        self.expected_5 = False
        self.actual_1 = self.recursor.is_palindrome('racecar')
        self.actual_2 = self.recursor.is_palindrome('kayak')
        self.actual_3 = self.recursor.is_palindrome('a')
        self.actual_4 = self.recursor.is_palindrome('library')
        self.actual_5 = self.recursor.is_palindrome('dngojkafnghkoasng')
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)
        self.assertEqual(self.actual_3, self.expected_3)
        self.assertEqual(self.actual_4, self.expected_4)
        self.assertEqual(self.actual_5, self.expected_5)

    def test_find_next_palindrome(self):
        self.expected_1 = 101
        self.expected_2 = 292
        self.actual_1 = self.recursor.find_next_palindrome(100)
        self.actual_2 = self.recursor.find_next_palindrome(283)
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)

    def test_palindromic_sum(self):
        self.expected = [
            209, 308, 407, 506, 605, 704, 803, 902, 1000, 1001, 1002, 1003, \
            1004, 1005, 1006, 1007, 1008, 1010, 1011, 1012, 1013, 1014, 1015, \
            1016, 1017
        ]
        self.actual = self.recursor.palindromic_sum(25)
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(len(self.actual), 25)

    def test_flattener(self):
        self.expected_1 = [1, 2, 3, 4, 5, 6]
        self.expected_2 = ['hi', 'this is', 'a', 'string', 'that is very', 'nested']
        self.actual_1 = self.recursor.flattener([1, 2, 3, [[4], 5], [[[6]]]])
        self.actual_2 = self.recursor.flattener(['hi', 'this is', [[['a', 'string'], 'that is very'], [[[['nested']]]]]])
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)

    def test_nth_fibonnaci(self):
        self.expected_1 = 1
        self.expected_2 = 8
        self.expected_3 = 13
        self.expected_4 = 21
        self.expected_5 = 12586269025
        self.actual_1 = self.recursor.nth_fibonnaci(2)
        self.actual_2 = self.recursor.nth_fibonnaci(6)
        self.actual_3 = self.recursor.nth_fibonnaci(7)
        self.actual_4 = self.recursor.nth_fibonnaci(8)
        self.actual_5 = self.recursor.nth_fibonnaci(50)
        self.assertEqual(self.actual_1, self.expected_1)
        self.assertEqual(self.actual_2, self.expected_2)
        self.assertEqual(self.actual_3, self.expected_3)
        self.assertEqual(self.actual_4, self.expected_4)
        self.assertEqual(self.actual_5, self.expected_5)

    #
    # print('valid_grid_traveler_combos:')
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 1), 0))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 0), 0))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 2), 0))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(2, 0), 0))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 0), 0))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 1), 1))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 3), 1))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 1), 1))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(2, 3), 3))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 2), 3))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 3), 6))
    # print(Recursor.test_func(Recursor.valid_grid_traveler_combos(18, 18), 2333606220))
    # print('\n')
    #
    # print('can_sum:')
    # print(Recursor.test_func(Recursor.can_sum(7, [2, 3]), True))
    # print(Recursor.test_func(Recursor.can_sum(7, [5, 3, 4, 7]), True))
    # print(Recursor.test_func(Recursor.can_sum(7, [2, 4]), False))
    # print(Recursor.test_func(Recursor.can_sum(8, [2, 3, 5]), True))
    # print(Recursor.test_func(Recursor.can_sum(300, [7, 14]), False))
    # print('\n')
    #
    # print('how_sum:')
    # print(Recursor.test_func(Recursor.how_sum(7, [2, 3]), [2, 2, 3]))
    # print(Recursor.test_func(Recursor.how_sum(7, [5, 3, 4, 7]), [3, 4]))
    # print(Recursor.test_func(Recursor.how_sum(7, [2, 4]), None))
    # print(Recursor.test_func(Recursor.how_sum(8, [2, 3, 5]), [3, 5]))
    # print(Recursor.test_func(Recursor.how_sum(0, [1, 2, 3]), []))
    # print(Recursor.test_func(Recursor.how_sum(300, [7, 14]), None))
    # print('\n')
    #
    # print('best_sum:')
    # print(Recursor.test_func(Recursor.best_sum(7, [2, 4]), None))
    # print(Recursor.test_func(Recursor.best_sum(7, [5, 3, 4, 7]), [7]))
    # print(Recursor.test_func(Recursor.best_sum(8, [2, 3, 5]), [3, 5]))
    # print(Recursor.test_func(Recursor.best_sum(0, [1, 2, 3]), []))
    # print(Recursor.test_func(Recursor.best_sum(100, [1, 2, 5, 25]), [25, 25, 25, 25]))
    # print('\n')



if __name__ == '__main__':
    unittest.main(verbosity=2)
