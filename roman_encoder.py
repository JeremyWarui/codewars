"""
Program that converts the integer into roman numerals.

For example:
   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"

KEY:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

"""


def roman_encoder(n):
    """
    solution: returns roman numerals from an integer

    :param n: integer(btween 1 - 3999) that is to be converted to roman numerals
    """
    roman_values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = []
    for (value, symbol) in roman_values:
        while n >= value:
            result.append(symbol)
            n = n - value
    return "".join(result)


print(roman_encoder(1))
print(roman_encoder(1000))
print(roman_encoder(1666))
print(roman_encoder(2000))
print(roman_encoder(2026))
