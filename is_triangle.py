"""
Determine if its a triangle or not.
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
"""


def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if (a + b) > c and (b + c) > a and (c + a) > b:
            return True
    return False


print(is_triangle(1, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(2, 2, 2))
print(is_triangle(1, 2, 3))
print(is_triangle(-5, 1, 3))
print(is_triangle(0, 2, 3))
print(is_triangle(1, 2, 9))
