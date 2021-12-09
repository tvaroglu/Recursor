import unittest
from lib.recursor import Recursor

class TestRecursor(unittest.TestCase):
    def setUp(self):
        self.recursor = Recursor()

    def test_test(self):
        self.assertEqual(True, True)


# if __name__ == '__main__':
#     unittest.main()
if __name__ == '__main__':
    unittest.main(verbosity=2)
