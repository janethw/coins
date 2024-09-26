from denominations import Denomination


def main():
    value = 10 ** 2
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # Validate value (V)
    try:
        print(f"{value=}")
        check_value_is_valid(value)
    except ValueError as value_error:
        print(f"Value is not valid: {value_error}")

    # Validate coins array
    try:
        check_coins_array_is_valid(coins)
    except ValueError as value_error:
        print(f"The coins array is not valid: {value_error}")


# Check target value is in range
def check_value_is_in_range(input_value):
    if not (0 <= input_value <= 10 ** 15):
        print(-1)
        raise ValueError("Value, V, must be between 0 and 10 to the power 15")  # Equivalent to GBP 10 Trillion
    return input_value


# Check target value is an integer
def check_value_is_int(input_value):
    if not isinstance(input_value, int):
        print(-1)
        raise ValueError("Value, V, must be expressed in terms of unit currency, "
                         "eg whole pence for Pound Sterling")
    return input_value


# Check target value is positive or zero
def check_value_is_positive_or_zero(input_value):
    if input_value < 0:
        print(-1)
        raise ValueError("Value, V, must be positive or zero")
    return input_value


def check_value_is_valid(input_value):
    check_value_is_in_range(input_value)
    check_value_is_int(input_value)
    check_value_is_positive_or_zero(input_value)
    return input_value


def check_coins_array_is_valid(coins):
    check_for_duplicates()
    check_array_length()
    check_large_denominations()
    check_positive_integers()
    return coins


# Validation of coins[] - check denominations are positive integers
def check_positive_integers():
    pass


# Validation of coins[] - removal of duplicates
def check_for_duplicates():
    pass


# Validation of coins[] - check of array length
def check_array_length():
    pass


# Validation of coins[] - check of denomination amounts
def check_large_denominations():
    pass


if __name__ == "__main__":
    main()
