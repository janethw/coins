import unittest

from coins import (check_value_is_int, check_value_is_positive_or_zero, check_value_is_in_range, remove_duplicates,
                   check_coins_is_list)


class TestTargetValue(unittest.TestCase):

    def test_check_value_is_in_range(self):
        # Positive test case
        self.assertLessEqual(check_value_is_in_range(10 ** 15), 10 ** 15)
        self.assertLessEqual(check_value_is_int(12 ** 4), 12 ** 4)
        self.assertLessEqual(check_value_is_int(12), 12)

        # Negative test case
        negative_test_cases_for_range = [-1, 10 ** 16, -10 ** 16, -4 ** 11]
        for test_value in negative_test_cases_for_range:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_in_range(test_value)
            self.assertEqual(str(context.exception),
                             "Value, V, must be between 0 and 10 to the power 15")

    def test_input_value_is_an_int(self):
        # Positive test case
        self.assertIsInstance(check_value_is_int(4), int)
        self.assertIsInstance(check_value_is_int(-2), int)
        self.assertIsInstance(check_value_is_int(10 ** 15), int)
        self.assertIsInstance(check_value_is_int(10 ** 16), int)

        # Negative test case
        # self.assertIsInstance(check_value_is_int(4.23 * 100), int)  # AssertionError: 423.00000000000006 is not an instance of <class 'int'>
        # self.assertIsInstance(check_value_is_int(4.23 * 100 % 100), int)  # AssertionError: 23.000000000000057 is not an instance of <class 'int'>
        negative_test_cases_for_int = [4.23, 4.23**3, 4.23 * 100, 4.23 * 100 % 100]
        for test_value in negative_test_cases_for_int:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_int(test_value)
            self.assertEqual(str(context.exception),
                             "Value, V, must be expressed in terms of unit currency, eg whole pence for Pound Sterling")

    def test_input_value_is_positive_or_zero(self):
        # Positive test case
        self.assertEqual(check_value_is_positive_or_zero(5), 5)
        self.assertEqual(check_value_is_positive_or_zero(0), 0)

        # # Negative test case
        with self.assertRaises(ValueError) as context:
            check_value_is_positive_or_zero(-4)
        self.assertEqual(str(context.exception), "Value, V, must be positive or zero")


class TestDenominationClass(unittest.TestCase):

    def test_check_coins_is_list(self):
        # Positive test case of instance
        self.assertIsInstance(check_coins_is_list([2, 5, 10]), list)
        self.assertIsInstance(check_coins_is_list([0, 1, 2, 2, 5, 10, 100]), list)

        # Negative test case of instance
        with self.assertRaises(ValueError) as context:
            check_coins_is_list({0, 1, 2, 25, 10, 10})
        self.assertEqual(str(context.exception), "Coin denominations must be in a list")

    def test_remove_duplicates(self):
        # Positive test case of output
        self.assertEqual(remove_duplicates([2, 5, 10]), [2, 5, 10])
        self.assertEqual(remove_duplicates([0, 1, 2, 2, 2, 5, 10, 100]), [0, 1, 2, 5, 10, 100])
        self.assertEqual(remove_duplicates([1, 1, 1, 2, 5, 10, 50, 100, 200, 200, 200, 2 * 10 ** 2]),
                         [1, 2, 5, 10, 50, 100, 200])


if __name__ == "__main__":
    unittest.main()
