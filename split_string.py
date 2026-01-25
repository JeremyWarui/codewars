# split string into even array of strings

# 'abcdef' => ['ab', 'cd', 'ef']

str = "abcde"


def split_string(str):
    """function that splits strings into even elements from the string"""
    # 1. loop through the string to split after two characters
    # then append the two characters to the array.
    pairs = []
    i = 0
    if len(str) % 2 != 0:
        str += "_"

    while i < len(str):
        pair = str[i : i + 2]
        pairs.append(pair)
        i += 2

    print(pairs)


split_string(str)
