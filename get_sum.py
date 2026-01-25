"""
Docstring for get_sum

(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""


def get_sum(a, b):
    """
    Docstring for get_sum

    :param a: Description
    :param b: Description
    """
    # sum = 0
    # for i in range(min(a, b), max(a, b) + 1):
        # print(f"a:{a},b: {b}")
        # if a == b:
            # return a
        # sum += i
        # print(f"sum: {sum}, i = {i}")

    # return sum
    return sum(range(min(a,b), (max(a,b) + 1)))




print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
print(get_sum(2,2))
