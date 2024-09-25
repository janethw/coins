def main():
    value = -2
    try:
        check_value_is_int(value)
        check_value_is_positive_or_zero(value)
    except ValueError as value_error:
        print(f"Value is not valid; {value_error}")


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


if __name__ == "__main__":
    main()
