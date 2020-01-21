import random
import numpy as np
from .mst import mst


MAX_DIST = 10000

def greedy(grid):

    clear(grid)

    # init
    num_houses = 0
    random.shuffle(grid.batteries)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    for battery in grid.batteries:

        closest_house_index = pick(battery)
        # keep making connections until capacity is reached
        while check_cap(battery, grid.houses[closest_house_index]):

            # get index of closest house to battery
            closest_house_index = pick(battery)

            # if all houses are connected break out of loop
            if battery.distances[closest_house_index] == MAX_DIST:
                break

            remove_house(grid, closest_house_index)
            battery.houses.append(grid.houses[closest_house_index])

        num_houses += len(battery.houses)



    print(num_houses)
    if num_houses < len(grid.houses):
        greedy(grid)
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
    closest_index = battery.distances.index(min(battery.distances))
    return closest_index


def check_cap(battery, house):
    if (battery.capacity_used() + house.output) <= battery.capacity:
        return True


def remove_house(grid, closest_index):
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST


# def draw(grid):
#     for battery in grid.batteries:
#         for house in battery.houses:
#             house.battery = battery
#             house.add_cable()
