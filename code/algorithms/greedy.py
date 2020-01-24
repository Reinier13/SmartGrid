import random
import numpy as np
from .mst import mst


MAX_DIST = 10000

def greedy(grid):
    """
    Greedy algorithm that chooses a random battery and connects with houses
    that are closest until the capacity of the battery is reached.
    """

    # clears all lists in the grid
    clear(grid)

    # init
    num_houses = 0
    random.shuffle(grid.batteries)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    for battery in grid.batteries:

        # get index of closest house to battery
        closest_house_index = pick(battery)

        # keep making connections until capacity is reached
        while check_cap(battery, grid.houses[closest_house_index]):
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


def clear(grid):
    """
    Clears all lists in grid.
    """
    for battery in grid.batteries:
        battery.houses = []
        battery.distances = []
    for house in grid.houses:
        house.battery = None
        house.cables = []

def distance(house, battery):
    """
    Calculates distance between house and battery.
    """
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta


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


def check_cap(battery, house):
    """
    Checks if capacity of battery is yet reached.
    """
    if (battery.capacity_used() + house.output) <= battery.capacity:
        return True


def remove_house(grid, closest_index):
    """
    Marks house as connected to a battery.
    """
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST


def draw(grid):
    """
    Adds all grid points to a list, which form the cable from house to battery.
    """
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
