def main():
    value = 10 ** 2

    try:
        print(f"{value=}")
        check_value_is_valid(value)
    except ValueError as value_error:
        print(f"Value is not valid; {value_error}")


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


if __name__ == "__main__":
    main()
