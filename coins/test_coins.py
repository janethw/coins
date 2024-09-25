import unittest

from coins import check_value_is_int, check_value_is_positive_or_zero


class TestTargetValue(unittest.TestCase):

    def test_input_value_is_an_int(self):
        # Positive test case
        self.assertIsInstance(check_value_is_int(4), int)
        self.assertIsInstance(check_value_is_int(-2), int)

        # Negative test case
        # self.assertIsInstance(check_value_is_int(4.23 * 100), int)  # AssertionError: 423.00000000000006 is not an instance of <class 'int'>
        # self.assertIsInstance(check_value_is_int(4.23 * 100 % 100), int)  # AssertionError: 23.000000000000057 is not an instance of <class 'int'>
        # self.assertIsInstance(check_value_is_int(4.0), int)  # AssertionError: 4.0 is not an instance of <class 'int'>

    def test_input_value_is_positive_or_zero(self):
        # Positive test case
        self.assertEqual(check_value_is_positive_or_zero(5), 5)
        self.assertEqual(check_value_is_positive_or_zero(0), 0)

        # # Negative test case
        with self.assertRaises(ValueError) as context:
            check_value_is_positive_or_zero(-4)
        self.assertEqual(str(context.exception), "Value, V, must be positive or zero")


if __name__ == "__main__":
    unittest.main()
