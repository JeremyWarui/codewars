"""
Growth of a population
Expected output:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
"""


def nb_year(p0, percent, aug, p):
    """
    nb_year: returns the no of years it takes for population to grow to the expected target.

    :param p0: Initial population
    :param percent: percentage growth each year(%)
    :param aug: Yearly incrememnt of population in numbers
    :param p: expected target of population to be reached in the no of years
    """
    new_population = p0
    years = 0

    while new_population < p:
        years += 1
        new_population = int(new_population + ((percent / 100) * new_population) + aug)

    return years


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
