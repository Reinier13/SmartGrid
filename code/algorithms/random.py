import random


def random_connection(grid):
    for house in grid.houses:
        key = random.choice(list(grid.batteries))
        grid.batteries[key].add_house(house)
