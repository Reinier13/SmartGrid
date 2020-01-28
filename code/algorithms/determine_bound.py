import random
import numpy as np
from code.helpers import distance


def determine_bound(grid):
    """
    Determine bound is an algorithm that connects every house to it's closest
    or furthest battery, without a capacity constraint for the battery.

    This is useful to determine the lower and upperbound
    for the state space in mission 1 & 2.
    """
    global counter
    random.shuffle(grid.houses)
    for house in grid.houses:
        counter = 0
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))
        find_battery(house, grid.batteries, grid)
    grid.draw()


def find_battery(house, batteries, grid):
    """
    Connect the furthest or closest battery, dependent on the global counter,
    to a house.
    """
    global counter
    distances = np.array(house.distances)
    closest = house.distances.index(np.partition(distances, counter)[counter])

    house.battery = batteries[closest]
    house.battery.add_house(house)
