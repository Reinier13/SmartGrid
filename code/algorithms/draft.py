import random
import numpy as np


MAX_DIST = 10000


def draft(grid):
    """
    Draft - Greedy algorithm that connects the batteries in turn with the houses
    that are closest to that battery until the capacity of the battery is reached.
    """

    # init
    num_houses = 0
    random.shuffle(grid.batteries)

    # clear all lists in grid
    clear(grid)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    house_available = True
    while house_available:
        for battery in grid.batteries:

            # get index of closest house
            closest_house_index = pick(battery)

            # add house if capacity is not yet reached
            if check_cap(battery):

                # end algorithm if all houses are connected
                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break

                # connect house to battery and mark as connected
                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
                num_houses += 1

    # run again if not all houses connected otherwise draw up grid
    if num_houses < len(grid.houses):
        draft(grid)
    else:
        draw(grid)


def clear(grid):
    for battery in grid.batteries:
        battery.houses = []
        battery.distances = []
    for house in grid.houses:
        house.battery = None
        house.cables = []

def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta


def create_distances(grid):
    for battery in grid.batteries:
        for house in grid.houses:
            battery.distances.append(distance(house, battery))


def pick(battery):
    closest_house_index = battery.distances.index(min(battery.distances))
    return closest_house_index


def check_cap(battery):
    if battery.capacity_used() <= battery.capacity:
        return True


def remove_house(grid, closest_house_index):
    for battery in grid.batteries:
        battery.distances[closest_house_index] = MAX_DIST


def draw(grid):
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
