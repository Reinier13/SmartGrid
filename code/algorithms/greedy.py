import random
import numpy as np
from .mst import mst


MAX_DIST = 10000

def greedy(grid):
    # init
    num_houses = 0

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    for battery in grid.batteries:

        # keep making connections until capacity is reached
        while check_cap(battery):

            # get index of closest house to battery
            closest_index = pick(battery)

            # if all houses are connected break out of loop
            if battery.distances[closest_index] == MAX_DIST:
                break

            remove_house(grid, closest_index)
            battery.houses.append(grid.houses[closest_index])
<<<<<<< HEAD
    mst(grid)

    # draw(grid)
=======
        num_houses += len(battery.houses)

    draw(grid)
>>>>>>> 94754e690ba85a9b39b50394d085f67f8d2cd80a


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
    closest_index = battery.distances.index(min(battery.distances))
    return closest_index


def check_cap(battery):
    if battery.capacity_used() <= battery.capacity:
        return True


def remove_house(grid, closest_index):
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST


<<<<<<< HEAD
# def draw(grid):
#     for battery in grid.batteries:
#         for house in battery.houses:
#             house.battery = battery
#             house.add_cable()
=======
def draw(grid):
    # for house in grid.houses:
    #     house.battery = None
    #     house.cables = []
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
>>>>>>> 94754e690ba85a9b39b50394d085f67f8d2cd80a
