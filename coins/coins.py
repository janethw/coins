from denominations import Denomination


def main():
    valueV = 10 ** 2
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    max_denominations = 10 ** 3  # Used to set max length to coins array

    # Validate value (V)
    try:
        print(f"{valueV=}")
        check_value_is_valid(valueV, variable_name="V")
    except ValueError as value_error:
        print(-1)
        print(f"Value is not valid: {value_error}")

    # Validate that coins is a list
    try:
        check_coins_is_list(coins)
    except ValueError as value_error:
        print(-1)
        print(f"Coin array is not valid: {value_error}")

    # Remove duplicates from coins array
    try:
        coins = remove_duplicates(coins)
    except ValueError as value_error:
        print(-1)
        print(f"The coins array is not valid: {value_error}")

    # Check coins array length within limits
    try:
        check_array_length(coins, variable_name="coins array", max_array_length=max_denominations)
    except ValueError as value_error:
        print(-1)
        print(f"Coin array is not valid: {value_error}")

    # Validate coins array
    try:
        check_coins_array_is_valid(coins, variable_name="coins array")
    except ValueError as value_error:
        print(-1)
        print(f"The coins array is not valid: {value_error}")


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


if __name__ == "__main__":
    main()
