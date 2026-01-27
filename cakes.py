"""
Program that returns no of cakes on can bake given the recipe and the available ingredients required to bake the cakes.
"""


def cakes(recipe, available):
    """
    cakes: returns the number of cakes that can be baked given the recipe and the available ingredients

    :param recipe: the ingredients required for the recipe
    :param available: the available ingredients that can be used to bake a cake
    """
    # check if all items in recipe are available in available dict
    # if there are some not present, return 0
    # else if they are present, divide with the available values and append in the list
    #  find the minimum no from the list

    # possible_cakes = []
    # for item, quantity in recipe.items():
    #     if item not in available:
    #         return 0
    #     possible_cakes.append(available[item] // quantity)

    # return min(possible_cakes)
    return min(available.get(item, 0) // quantity for item, quantity in recipe.items())


print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)
# must return 0
print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)
