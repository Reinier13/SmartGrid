import random


def random_connection(grid):
    for house in grid.houses:
        assigned_battery = random.choice(list(grid.batteries))
        assigned_battery.add_house(house)
