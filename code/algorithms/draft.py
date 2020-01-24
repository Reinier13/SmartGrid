import random
import numpy as np
from code.algorithms.helpers import distance


MAX_DIST = 10000


def draft(grid):

    for battery in grid.batteries:
        battery.clear()
        for house in battery.houses:
            house.clear()

    num_houses = 0
    random.shuffle(grid.batteries)

    create_distances(grid)

    house_available = True
    while house_available:

        for battery in grid.batteries:
            closest_house_index = pick(battery)
            if battery.check_cap(grid.houses[closest_house_index]):

                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break

                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
                num_houses += 1

    if num_houses < len(grid.houses):
        draft(grid)
    else:
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


def draw(grid):
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
