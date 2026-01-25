"""
Square Digits Module

This module provides functions for generating square numbers.
"""


def square_digits(num):
    """
    Calculate the square of a given number.

    Args:
        num (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    # num_string = str(num)
    # squared_nums = [ int(digit) ** 2 for digit in num_string ]
    return int("".join(map(str, [int(digit) ** 2 for digit in str(num)])))


if __name__ == "__main__":
    print(square_digits(9119))
