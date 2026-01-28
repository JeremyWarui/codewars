"""
Docstring for alphabet_position
"""


def alphabet_position(text):
    """
    Function: alphabet_position. Returns a string of numbers replacing the position of the alphabet.

    :param text: The string that the alphabets that need to be replaced with numerical values
    """

    # alphabet_values = {
    #     "a": 1,
    #     "b": 2,
    #     "c": 3,
    #     "d": 4,
    #     "e": 5,
    #     "f": 6,
    #     "g": 7,
    #     "h": 8,
    #     "i": 9,
    #     "j": 10,
    #     "k": 11,
    #     "l": 12,
    #     "m": 13,
    #     "n": 14,
    #     "o": 15,
    #     "p": 16,
    #     "q": 17,
    #     "r": 18,
    #     "s": 19,
    #     "t": 20,
    #     "u": 21,
    #     "v": 22,
    #     "w": 23,
    #     "x": 24,
    #     "y": 25,
    #     "z": 26,
    # }

    # nums = [str(i) for i in range(1, 27)]
    # print(nums)
    # chars = list("abcdefghijklmnopqrstuvwxyz")
    # alphabets_and_values = dict(zip(chars, nums))
    # print(alphabets_and_values)

    # result = [
    #     alphabet_values.get(letter_lower)
    #     for letter in text
    #     if (letter_lower := letter.lower()) in alphabet_values
    # ]
    # return " ".join(map(str, result))

    result = [
        # (ord(letter.lower()) - ord("a") + 1) for letter in text if letter.isalpha()
        (ord(letter) - ord('a') + 1) for letter in text.lower() if letter.isalpha()
    ]
    # print(result)
    return " ".join(map(str, result))


print(alphabet_position("abcdef"))
print(alphabet_position("The sunset sets at twelve o' clock."))
