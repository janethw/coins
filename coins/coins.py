def main():
    max_array_length = 10 ** 3  # Used to set max length to coins array

    # Get user inputs coins array
    coins = get_currency_denomination_inputs()
    valueV = get_target_value_input()

    # Validate valueV (V)
    try:
        check_value_is_valid(valueV, variable_name="V")
    except ValueError as value_error:
        print(-1)
        print(f"Value is not valid: {value_error}")

    # Validate coins array
    # Check coins array is a list
    try:
        check_coins_is_list(coins)
    except ValueError as value_error:
        print(-1)
        print(f"Coin array is not valid: {value_error}")

    # Remove any duplicates from coins array
    try:
        coins = remove_duplicates(coins)
    except ValueError as value_error:
        print(-1)
        print(f"The coins array is not valid: {value_error}")

    # Check coins array length within array length limits
    try:
        check_array_length(coins, variable_name="coins array", max_array_length=max_array_length)
    except ValueError as value_error:
        print(-1)
        print(f"Coin array is not valid: {value_error}")

    # Additional validation of coins array
    try:
        check_coins_array_is_valid(coins, variable_name="coins array")
    except ValueError as value_error:
        print(-1)
        print(f"The coins array is not valid: {value_error}")

    # Find minimum number of coins required to make the target value,
    coins_dict = dict.fromkeys(coins, 0)
    # print(coins_dict)
    minimum_coins_dict = calculate_minimum_coins_for_target_value(valueV, coins, coins_dict)

    # Check target value was achieved with the given currency denominations
    if not check_target_value_was_achieved_with_given_currency(valueV, minimum_coins_dict):
        print("-1\nThe target value cannot be achieved with the given currency denominations.")
    else:
        # print(f"After min_coins_dict fn call, {minimum_coins_dict=}")
        print(f"\nThe minimum coins to achieve the target value {valueV} is: ")
        for k, v in minimum_coins_dict.items():
            if v != 0:
                print(f"{v} x coin {k}")
        print(f"The total number of coins required is {sum(minimum_coins_dict.values())}")


def get_currency_denomination_inputs():
    coins_array = []
    while True:
        denominations = input("Enter denominations as integers separated by space: ")
        denominations = denominations.split(" ")
        try:
            for denomination in denominations:
                coins_array.append(int(denomination))
        except ValueError:
            print("Denominations were invalid - they need to be integers separated by spaces.")
            coins_array = []
        else:
            sorted_coins_array = sorted(coins_array)
            print(f"The currency denominations you have set are: {sorted_coins_array}")
            return sorted_coins_array


def get_target_value_input():
    while True:
        try:
            valueV = int(input("Enter the target value, V, as an integer: "))
        except ValueError:
            print("Value, V, is invalid - it needs to be an integer.")
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


# Check target value is in range
def check_value_is_in_range(input_value, variable_name):
    if not (0 <= input_value <= 10 ** 15):
        print(-1)
        raise ValueError(f"Currency amounts for {variable_name} must be between 0 and 10 to the power 15")  # Equivalent to GBP 10 Trillion
    return input_value


# Check target value is an integer
def check_value_is_int(input_value, variable_name):
    if not isinstance(input_value, int):
        print(-1)
        raise ValueError(f"Currency amounts for {variable_name} must be expressed in terms of unit currency, "
                         "eg multiples of whole pence for Pound Sterling")
    return input_value


# Check target value is positive or zero
def check_value_is_positive(input_value, variable_name):
    if input_value <= 0:
        print(-1)
        raise ValueError(f"Currency amounts for {variable_name} must be positive")
    return input_value


def check_coins_array_is_valid(coins, variable_name):
    for coin in coins:
        check_value_is_int(coin, variable_name)
        check_value_is_in_range(coin, variable_name)
    return coins


# Validation of coins[] - check type is list
def check_coins_is_list(coins):
    if not isinstance(coins, list):
        print(-1)
        raise ValueError("Coin denominations must be in a list")
    return coins


# Validation of coins[] - removal of duplicates
def remove_duplicates(coin_array):
    unique_coin_array = []
    for coin in coin_array:
        if coin not in unique_coin_array:
            unique_coin_array.append(coin)
    return unique_coin_array


# Validation of coins[] - check of array length
def check_array_length(coins, variable_name, max_array_length):
    if len(coins) > max_array_length:
        print(-1)
        raise ValueError(f"{variable_name} can contain up to {max_array_length} denomination amounts")
    return coins


if __name__ == "__main__":
    main()
