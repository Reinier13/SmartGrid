import random
import numpy as np
from .mst import mst
from code.algorithms.helpers import distance, draw, clear


MAX_DIST = 10000

def greedy(grid):
    """
    Greedy algorithm that chooses a random battery and connects with houses
    that are closest until the capacity of the battery is reached.
    """

    # init
    clear(grid)

    num_houses = 0
    random.shuffle(grid.batteries)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    for battery in grid.batteries:

        # get index of closest house to battery
        closest_house_index = pick(battery)

        # keep making connections until capacity is reached
        while battery.check_cap():

            # get index of closest house to battery
            closest_house_index = pick(battery)

            # if all houses are connected break out of loop
            if battery.distances[closest_house_index] == MAX_DIST:
                break

            # connect house to battery and mark as connected
            battery.houses.append(grid.houses[closest_house_index])
            remove_house(grid, closest_house_index)

        num_houses += len(battery.houses)

    # if not all houses are connected run again otherwise draw grid
    if num_houses < len(grid.houses):
        greedy(grid)
    else:
        draw(grid)


def create_distances(grid):
    """
    Creates lists of distances for all batteries to all houses.
    """
    for battery in grid.batteries:
        for house in grid.houses:
            battery.distances.append(distance(house, battery))


def pick(battery):
    """
    Gets the index of closest house to a battery.
    """
    closest_index = battery.distances.index(min(battery.distances))
    return closest_index


def remove_house(grid, closest_index):
    """
    Marks house as connected to a battery.
    """
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST
