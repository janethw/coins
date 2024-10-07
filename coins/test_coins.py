import unittest
from unittest.mock import patch

from coins import (check_value_is_int, check_value_is_positive, check_value_is_in_range,
                   check_coins_is_list, check_array_length, get_currency_denomination_inputs, get_target_value_input,
                   calculate_minimum_coins_for_target_value, check_target_value_was_achieved_with_given_currency)


class TestTargetValueClass(unittest.TestCase):

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

        # Negative test case
        negative_test_cases_for_positive = [-3, 0, -10**10, -7**3]
        for test_value in negative_test_cases_for_positive:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_positive(test_value, variable_name)
            self.assertEqual(str(context.exception), f"Currency amounts for {variable_name} must be positive")


class TestCoinsArrayClass(unittest.TestCase):

    def test_check_coins_is_list(self):
        # Positive test case of instance of list
        self.assertIsInstance(check_coins_is_list([2, 5, 10]), list)
        self.assertIsInstance(check_coins_is_list([0, 1, 2, 2, 5, 10, 100]), list)

        # Negative test case of instance of list
        negative_test_cases_for_list = [{1, 2, 10, 50}, (1, 2, 10, 50), "1, 2, 10, 50", 40]
        for test_value in negative_test_cases_for_list:
            print(f"Current test: {test_value=}")
            with self.assertRaises(TypeError) as context:
                check_coins_is_list(test_value)
            self.assertEqual(str(context.exception), "Coin denominations must be in a list")

    def test_coin_value_is_positive(self, variable_name="coins array"):
        # Positive test case for coin in coins array
        self.assertEqual(check_value_is_positive(1000, variable_name), 1000)
        self.assertEqual(check_value_is_positive(2, variable_name), 2)

        # Negative test case for coin in coins array
        negative_test_cases_for_positive_coins = [-400, 0, -10 ** 10, -7 ** 3]
        for test_value in negative_test_cases_for_positive_coins:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_positive(test_value, variable_name)
            self.assertEqual(str(context.exception), f"Currency amounts for {variable_name} must be positive")

    def test_check_value_is_in_range(self, variable_name="coins array"):
        # Positive test case for coin in coins array
        self.assertLessEqual(check_value_is_in_range(10 ** 14, variable_name), 10 ** 14)
        self.assertLessEqual(check_value_is_in_range(12 ** 6, variable_name), 12 ** 6)
        self.assertLessEqual(check_value_is_in_range(19, variable_name), 19)

        # Negative test case
        negative_test_cases_for_range = [-5, 10 ** 16, -10 ** 16, -4 ** 11]
        for test_value in negative_test_cases_for_range:
            print(f"Current test: {test_value=}")
            with self.assertRaises(ValueError) as context:
                check_value_is_in_range(test_value, variable_name)
            self.assertEqual(str(context.exception),
                             f"Currency amounts for {variable_name} must be between 0 and 10 to the power 15")

    def test_check_array_length(self, variable_name="coins array", max_array_length=10):
        # Positive test case
        self.assertEqual(check_array_length([1, 2, 5, 10, 20, 50], variable_name, max_array_length), [1, 2, 5, 10, 20, 50])
        self.assertEqual(check_array_length([1, 2, 5, 10, 20, 50, 100, 1000], variable_name, max_array_length), [1, 2, 5, 10, 20, 50, 100, 1000])
        self.assertLessEqual(check_array_length([], variable_name, max_array_length), [])

        # Negative test case
        negative_test_cases_for_len_coins_array = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
        for test_case in negative_test_cases_for_len_coins_array:
            with self.assertRaises(ValueError) as context:
                check_array_length(test_case, variable_name, max_array_length)
            self.assertEqual(str(context.exception),
                             f"{variable_name} can contain up to {max_array_length} denomination amounts")


class TestUserInputsClass(unittest.TestCase):

    # Test of user inputs for coins array, coins[]
    @patch("builtins.input", return_value="1 2 5 10", autospec=True)
    def test_get_currency_denomination_inputs_converts_to_list(self, mock_input):
        result = get_currency_denomination_inputs(max_array_length=10**3)
        expected_result = [1, 2, 5, 10]
        self.assertEqual(result, expected_result)

    @patch("builtins.input", return_value="10 5 2 1", autospec=True)
    def test_get_currency_denomination_inputs_order_sorted_1(self, mock_input):
        result = get_currency_denomination_inputs(max_array_length=10**3)
        expected_result = [1, 2, 5, 10]
        self.assertEqual(result, expected_result)

    @patch("builtins.input", return_value="2 10 5 1", autospec=True)
    def test_get_currency_denominations_inputs_order_sorted_2(self, mock_input):
        result = get_currency_denomination_inputs(max_array_length=10**3)
        expected_result = [1, 2, 5, 10]
        self.assertEqual(result, expected_result)

    @patch("builtins.input", return_value="4 3 2", autospec=True)
    def test_get_currency_denominations_inputs_order_sorted_3(self, mock_input):
        result = get_currency_denomination_inputs(max_array_length=10**3)
        expected_result = [2, 3, 4]
        self.assertEqual(result, expected_result)

    @patch("builtins.input", return_value="4 3 2 2", autospec=True)
    def test_get_currency_denominations_inputs_duplicates_removed(self, mock_input):
        result = get_currency_denomination_inputs(max_array_length=10 ** 3)
        expected_result = [2, 3, 4]
        self.assertEqual(result, expected_result)

    # Negative test case
    # @patch("builtins.input", return_value="one two five ten", autospec=True)
    # def test_get_currency_denomination_inputs_invalid(self, mock_input):
    #     print(f"{mock_input.call_count=}")
    #     # 1st invalid input mock
    #     result = get_currency_denomination_inputs()
    #     expected_result = "Denominations were invalid - they need to be integers separated by spaces."
    #     self.assertEqual(result, expected_result)

        # # 2nd invalid input mock
        # with self.assertRaises(ValueError) as context:
        #     get_currency_denomination_inputs()
        # self.assertEqual(str(context.exception),
        #                  "Denominations were invalid - they need to be integers separated by spaces.")
        #
        # # 3rd input (valid this time to break the while loop)
        # result = get_currency_denomination_inputs()
        # expected_result = [1]
        # self.assertEqual(result, expected_result)

    # @patch("builtins.input", return_value="-4 3 2", autospec=True)
    # def test_get_currency_denominations_inputs_5(self, mock_input):
    #     result = get_currency_denomination_inputs(max_array_length=10 ** 3)
    #     expected_result = "Denominations were invalid - they need to be positive integers separated by spaces."
    #     self.assertEqual(result, expected_result)

    # Test of user input for target value V
    # Positive test case
    @patch('builtins.input', return_value="135", autospec=True)
    def test_get_target_value_input(self, mock_input):
        result = get_target_value_input()
        expected_result = 135
        self.assertEqual(result, expected_result)

    # Negative test case
    # @patch('builtins.input', side_effect=["13.54", "1"], autospec=True)
    # def test_get_target_value_input_invalid(self, mock_input):
    #     with self.assertRaises(ValueError) as context:
    #         get_target_value_input()
    #     self.assertEqual(str(context.exception), "Value, V, is invalid - it needs to be an integer."


class TestMinimumCoinCalculationClass(unittest.TestCase):

    # Positive test case
    def test_calculate_minimum_coins_for_target_value_1(self):
        self.assertEqual(calculate_minimum_coins_for_target_value(
            63, [1, 2, 5, 10], coins_dict={1: 0, 2: 0, 5: 0, 10: 0}), {1: 1, 2: 1, 5: 0, 10: 6})

    def test_calculate_minimum_coins_for_target_value_2(self):
        self.assertEqual(calculate_minimum_coins_for_target_value(
            23, [2, 3, 4], coins_dict={2: 0, 3: 0, 4: 0}), {2: 0, 3: 1, 4: 5})

    def test_calculate_minimum_coins_for_target_value_3(self):
        self.assertEqual(calculate_minimum_coins_for_target_value(
            6, [1, 3, 4], coins_dict={1: 0, 3: 0, 4: 0}), {1: 0, 3: 2, 4: 0})

    def test_calculate_minimum_coins_for_target_value_4(self):
        self.assertEqual(calculate_minimum_coins_for_target_value(
            42363, [1, 2, 5, 10, 20, 50, 100, 200],
            coins_dict={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0}),
            {1: 1, 2: 1, 5: 0, 10: 1, 20: 0, 50: 1, 100: 1, 200: 211})


class TestTargetValueAchievedWithGivenCurrencyDenominations(unittest.TestCase):

    # Positive test case
    def test_check_target_value_was_achieved_with_given_currency(self):
        self.assertEqual(check_target_value_was_achieved_with_given_currency(
            63, {1: 1, 2: 1, 5: 0, 10: 6}), 1)

    def test_check_target_value_was_not_achieved_with_given_currency(self):
        self.assertEqual(check_target_value_was_achieved_with_given_currency(
            63, {2: 1, 5: 0, 10: 6}), 0)

    # Negative test case
    def test_check_target_value_was_achieved_with_given_currency_fail(self):
        self.assertEqual(check_target_value_was_achieved_with_given_currency(
            63, {2: 1, 5: 0, 10: "not a number"}), 0)


if __name__ == "__main__":
    unittest.main()
