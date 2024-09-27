import unittest

from coins import (check_value_is_int, check_value_is_positive, check_value_is_in_range, remove_duplicates,
                   check_coins_is_list)


class TestTargetCoinsArray(unittest.TestCase):

    def test_check_value_is_in_range(self, variable_name="V"):
        # Positive test case for valueV
        self.assertLessEqual(check_value_is_in_range(10 ** 15, variable_name), 10 ** 15)
        self.assertLessEqual(check_value_is_in_range(12 ** 4, variable_name), 12 ** 4)
        self.assertLessEqual(check_value_is_in_range(12, variable_name), 12)

        # Negative test case
        negative_test_cases_for_range = [-1, 10 ** 16, -10 ** 16, -4 ** 11]
        for test_value in negative_test_cases_for_range:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_in_range(test_value, variable_name)
            self.assertEqual(str(context.exception),
                             f"Currency amounts for {variable_name} must be between 0 and 10 to the power 15")

    def test_input_value_is_an_int(self, variable_name="V"):
        # Positive test case
        self.assertIsInstance(check_value_is_int(4, variable_name), int)
        self.assertIsInstance(check_value_is_int(-2, variable_name), int)
        self.assertIsInstance(check_value_is_int(10 ** 15, variable_name), int)
        self.assertIsInstance(check_value_is_int(10 ** 16, variable_name), int)

        # Negative test case
        negative_test_cases_for_int = [4.23, 4.23**3, 4.23 * 100, 4.23 * 100 % 100]
        for test_value in negative_test_cases_for_int:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_int(test_value, variable_name)
            self.assertEqual(str(context.exception),
                             f"Currency amounts for {variable_name} must be expressed in terms of unit currency, "
                             f"eg multiples of whole pence for Pound Sterling")
        # Examples of early test fails due to precision errors following use of floats
        # self.assertIsInstance(check_value_is_int(4.23 * 100), int)  # AssertionError:
        # 423.00000000000006 is not an instance of <class 'int'>
        # self.assertIsInstance(check_value_is_int(4.23 * 100 % 100), int)  # AssertionError:
        # 23.000000000000057 is not an instance of <class 'int'>

    def test_input_value_is_positive(self, variable_name="V"):
        # Positive test case for valueV
        self.assertEqual(check_value_is_positive(5, variable_name), 5)
        self.assertEqual(check_value_is_positive(1, variable_name), 1)

        # # Negative test case
        negative_test_cases_for_positive_int = [-3, 0, -10**10, -7**3]
        for test_value in negative_test_cases_for_positive_int:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_positive(-4, variable_name)
            self.assertEqual(str(context.exception), f"Currency amounts for {variable_name} must be positive")


class TestDenominationClass(unittest.TestCase):

    def test_check_coins_is_list(self):
        # Positive test case of instance of list
        self.assertIsInstance(check_coins_is_list([2, 5, 10]), list)
        self.assertIsInstance(check_coins_is_list([0, 1, 2, 2, 5, 10, 100]), list)

        # Negative test case of instance of list
        negative_test_cases_for_int = [{1, 2, 10, 50}, (1, 2, 10, 50), "1, 2, 10, 50", 40]
        for test_value in negative_test_cases_for_int:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_coins_is_list(test_value)
            self.assertEqual(str(context.exception), "Coin denominations must be in a list")

    def test_remove_duplicates(self):
        # Positive test case of output
        self.assertEqual(remove_duplicates([2, 5, 10]), [2, 5, 10])
        self.assertEqual(remove_duplicates([0, 1, 2, 2, 2, 5, 10, 100]), [0, 1, 2, 5, 10, 100])
        self.assertEqual(remove_duplicates([1, 1, 1, 2, 5, 10, 50, 100, 200, 200, 200, 2 * 10 ** 2]),
                         [1, 2, 5, 10, 50, 100, 200])

    def test_input_value_is_positive(self, variable_name="coins array"):
        # Positive test case for coins array
        self.assertEqual(check_value_is_positive(5, variable_name), 5)
        self.assertEqual(check_value_is_positive(1, variable_name), 1)

        # Negative test case


if __name__ == "__main__":
    unittest.main()
