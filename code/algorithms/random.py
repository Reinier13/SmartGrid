import random


def random_connection(grid):
    for house in grid.houses:
        chosen_battery = random.choice(grid.batteries)
        chosen_battery.add_house(house)
