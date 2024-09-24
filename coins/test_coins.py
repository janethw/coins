import unittest

from coins import coin_calculator


class TestTargetValue(unittest.TestCase):
    def test_input_value_is_positive_or_zero(self):
        self.assertEqual(coin_calculator(5), 5)
        self.assertEqual(coin_calculator(-4), -1, "Value must be a positive amount")
        self.assertEqual(coin_calculator(0), 0)

    def test_input_value_is_an_int(self):
        self.assertIsInstance(coin_calculator(4), int)
        self.assertIsInstance(coin_calculator(-2), int, "An int, but must be positive")
        self.assertIsInstance(coin_calculator(4.23 * 100), int)  # AssertionError: 423.00000000000006 is not an instance of <class 'int'>
        self.assertIsInstance(coin_calculator(4.23 * 100 % 100), int)  # AssertionError: 23.000000000000057 is not an instance of <class 'int'>
        self.assertIsInstance(coin_calculator(4.0), int)  # AssertionError: 4.0 is not an instance of <class 'int'>


if __name__ == "__main__":
    unittest.main()