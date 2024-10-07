def main():
    max_array_length = 10 ** 3  # Used to set max length to coins array

    # Get user inputs for the coins array and target value V
    coins = get_currency_denomination_inputs(max_array_length)
    valueV = get_target_value_input()

    # Set a count of zero for each denomination (coin) in coins_dict
    coins_dict = dict.fromkeys(coins, 0)

    # Find minimum number of coins required to make the target value,
    minimum_coins_dict = calculate_minimum_coins_for_target_value(valueV, coins, coins_dict)

    # Check target value was achieved with the given currency denominations
    if not check_target_value_was_achieved_with_given_currency(valueV, minimum_coins_dict):
        print("-1\nThe target value cannot be achieved with the given currency denominations.")
    else:
        print(f"\nThe minimum coins to achieve the target value {valueV} is: ")
        for k, v in minimum_coins_dict.items():
            if v != 0:
                print(f"{v} x coin {k}")
        print(f"The total number of coins required is {sum(minimum_coins_dict.values())}")


def get_currency_denomination_inputs(max_array_length):

    while True:
        coins_array = []
        denominations = input("Enter denominations as integers separated by space: ")
        denominations = denominations.split(" ")
        try:
            for denomination in denominations:
                if int(denomination) > 0:
                    coins_array.append(int(denomination))
                else:
                    raise ValueError
            sorted_coins_array = sorted(set(coins_array))
            check_coins_array_is_valid(sorted_coins_array, max_array_length)
            print(f"The currency denominations you have set are: {sorted_coins_array}")
            return sorted_coins_array
        except ValueError:
            print("Denominations were invalid - they need to be positive integers separated by spaces.")


def get_target_value_input():
    while True:
        try:
            valueV = int(input("Enter the target value, V, as an integer: "))
            if int(valueV) > 0:
                check_value_is_valid(valueV, variable_name="V")
            else:
                raise ValueError
        except ValueError:
            print("Value, V, is invalid - it needs to be a positive integer.")
        else:
            return valueV


def calculate_minimum_coins_for_target_value(valueV, coins, coins_dict):
    i = len(coins) - 1
    while i >= 0:
        # print(f"{coins=}")
        whole_multiple, remainder = divmod(valueV, coins[i])
        coins_dict[coins[i]] = whole_multiple
        valueV = remainder
        coins.pop()
        # print(f"{coins_dict=}")
        return calculate_minimum_coins_for_target_value(valueV, coins, coins_dict)
    # print(f"After while loop, {coins_dict=}")
    return coins_dict


def check_target_value_was_achieved_with_given_currency(valueV, minimum_coins_dict):
    def multiply_func(a, b):
        return a * b
    try:
        target_value = sum(map(multiply_func, minimum_coins_dict.values(), minimum_coins_dict.keys()))
        if target_value == valueV:
            return 1
    except (ValueError, TypeError):
        print("Invalid input into function.")
    return 0


def check_value_is_valid(input_value, variable_name):
    check_value_is_in_range(input_value, variable_name)
    check_value_is_int(input_value, variable_name)
    check_value_is_positive(input_value, variable_name)
    return input_value


def check_coins_array_is_valid(coins, max_array_length):
    # Check coins array is a list
    try:
        check_coins_is_list(coins)
    except TypeError as type_error:
        print(f"Coin array is not valid: {type_error}")
        return 0

    # Check coins array length within array length limits
    try:
        check_array_length(coins, variable_name="coins array", max_array_length=max_array_length)
    except ValueError as value_error:
        print(f"Coin array is not valid: {value_error}")
        return 0

    # Check each denomination (or coin) is an integer and within range
    for coin in coins:
        try:
            check_value_is_int(coin, variable_name="coins_array")
            check_value_is_in_range(coin, variable_name="coins_array")

        except ValueError as value_error:
            print(f"The coins array is not valid: {value_error}")
        return 0

    return coins


# Validation of valueV - check value is in range
def check_value_is_in_range(input_value, variable_name):
    if not (0 <= input_value <= 10 ** 15):
        raise ValueError(f"Currency amounts for {variable_name} must be between 0 and 10 to the power 15")  # Equivalent to GBP 10 Trillion
    return input_value


# Validation of value V - check value V is an integer
def check_value_is_int(input_value, variable_name):
    if not isinstance(input_value, int):
        raise ValueError(f"Currency amounts for {variable_name} must be expressed in terms of unit currency, "
                         "eg multiples of whole pence for Pound Sterling")
    return input_value


# Validation of value V - check int is positive
def check_value_is_positive(input_value, variable_name):
    if input_value <= 0:
        raise ValueError(f"Currency amounts for {variable_name} must be positive")
    return input_value


# Validation of coins[] - check type is list
def check_coins_is_list(coins):
    if not isinstance(coins, list):
        raise TypeError("Coin denominations must be in a list")
    return coins


# Validation of coins[] - check of array length
def check_array_length(coins, variable_name, max_array_length):
    if len(coins) > max_array_length:
        raise ValueError(f"{variable_name} can contain up to {max_array_length} denomination amounts")
    return coins


if __name__ == "__main__":
    main()
