import random
import numpy as np
from code.algorithms.helpers import distance, draw, clear


MAX_DIST = 10000


def draft(grid):
    """
    Draft - Greedy algorithm that connects the batteries in turn with the houses
    that are closest to that battery until the capacity of the battery is reached.
    """

    clear(grid)

    # init
    num_houses = 0
    random.shuffle(grid.batteries)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    house_available = True
    while house_available:
        for battery in grid.batteries:

            # get index of closest house
            closest_house_index = pick(battery)
            if battery.check_cap(grid.houses[closest_house_index]):

                # end algorithm if all houses are connected
                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break

                # connect house to battery and mark as connected
                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
                num_houses += 1

    draw(grid)


def create_distances(grid):
    for battery in grid.batteries:
        for house in grid.houses:
            battery.distances.append(distance(house, battery))


def pick(battery):
    closest_house_index = battery.distances.index(min(battery.distances))
    return closest_house_index


def remove_house(grid, closest_house_index):
    for battery in grid.batteries:
        battery.distances[closest_house_index] = MAX_DIST
