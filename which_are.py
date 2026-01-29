"""
Program that returns a sorted array r in lexicographical order of the strings in array1 that are substrings of array2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

"""


def in_array(array1, array2):
    """
    Returns: sorted array of strings in lexicographic order

    :param array1: array of strings that need to be sorted
    :param array2: array of strings that array1 are substrings.
    """
    # your code
    #  lets try:
    #  sorted, then we  try using checking substrings(string.contains)
    # result = []
    # for word in array1:
    #     for sub in array2:
    #         if word in sub:
    #             result.append(word)
    #             break
    # return sorted(result)
    # using sets for unique strings
    results = set()

    for word in array1:
        for sub in array2:
            if word in sub:
                results.add(word)
    return sorted(results)


a1 = ["cat", "dog", "bird"]
a2 = ["catalog", "hotdog", "birthday", "fish"]

list_1 = ["sun", "moon", "star"]
list_2 = ["cloud", "rain", "wind", "start", "moonlight"]

a3 = ["arp", "live", "strong"]
a4 = ["lively", "alive", "harp", "sharp", "armstrong"]

a5 = ["tarp", "mice", "bull"]
a6 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(array1=a1, array2=a2))
print(in_array(array1=list_1, array2=list_2))
print(in_array(a3, a4))
print(in_array(a5, a6))
