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

    
    # print('factorial:')
    # print(Recursor.test_func(Recursor.factorial(5), 120))
    # print('\n')
    #
    # print('reverse_string:')
    # print(Recursor.test_func(Recursor.reverse_string('Ariel'), 'leirA'))
    # print('\n')
    #
    # print('power:')
    # print(Recursor.test_func(Recursor.power(2, 4), 16))
    # print(Recursor.test_func(Recursor.power(8, 5), 32768))
    # print('\n')
    #
    # print('is_palindrome:')
    # print(Recursor.test_func(Recursor.is_palindrome('racecar'), True))
    # print(Recursor.test_func(Recursor.is_palindrome('kayak'), True))
    # print(Recursor.test_func(Recursor.is_palindrome('a'), True))
    # print(Recursor.test_func(Recursor.is_palindrome('library'), False))
    # print(Recursor.test_func(Recursor.is_palindrome('dngojkafnghkoasng'), False))
    # print('\n')
    #
    # print('find_next_palindrome:')
    # print(Recursor.test_func(Recursor.find_next_palindrome(100), 101))
    # print(Recursor.test_func(Recursor.find_next_palindrome(283), 292))
    # print('\n')
    #
    # print('palindromic_sum:')
    # print(Recursor.palindromic_sum(0))
    # print(Recursor.test_func(len(Recursor.palindromic_sum(0)), 25))
    # print('\n')
    #
    # print('flattener:')
    # print(Recursor.test_func(Recursor.flattener([1, 2, 3, [[4], 5], [[[6]]]]), [1, 2, 3, 4, 5, 6]))
    # print(Recursor.test_func(Recursor.flattener(["hi", "this is", [[["string"], "that is very"], [[[["nested"]]]]]]), ["hi", "this is", "string", "that is very", "nested"]))
    # print('\n')
    #
    # print('nth_fibonnaci:')
    # print(Recursor.test_func(Recursor.nth_fibonnaci(2), 1))
    # print(Recursor.test_func(Recursor.nth_fibonnaci(6), 8))
    # print(Recursor.test_func(Recursor.nth_fibonnaci(7), 13))
    # print(Recursor.test_func(Recursor.nth_fibonnaci(8), 21))
    # print(Recursor.test_func(Recursor.nth_fibonnaci(50), 12586269025))
    # print('\n')
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
