import unittest
from golf import Golf_check


class MyTestCase(unittest.TestCase):
    def test_something(self):
        golf = Golf_check()
        self.assertIsNotNone(golf.temperature_fahrenheit)


if __name__ == '__main__':
    unittest.main()
