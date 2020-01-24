import random
import numpy as np
<<<<<<< HEAD
from .mst import mst
from code.algorithms.helpers import distance

=======
>>>>>>> a0bcedc520526e4b6b839f29f196ec29248fdc3e


MAX_DIST = 10000

def greedy(grid):

    # init
    for battery in grid.batteries:
        battery.clear()
        for house in battery.houses:
            house.clear()

    num_houses = 0
    random.shuffle(grid.batteries)

    # get distances of batteries to houses
    create_distances(grid)

    # create connection between houses and batteries
    for battery in grid.batteries:

        closest_house_index = pick(battery)

        # keep making connections until capacity is reached
        while battery.check_cap(grid.houses[closest_house_index]):

            # get index of closest house to battery
            closest_house_index = pick(battery)

            # if all houses are connected break out of loop
            if battery.distances[closest_house_index] == MAX_DIST:
                break

            remove_house(grid, closest_house_index)
            battery.houses.append(grid.houses[closest_house_index])

        num_houses += len(battery.houses)


    if num_houses < len(grid.houses):
        greedy(grid)
    else:
        draw(grid)


def create_distances(grid):
    for battery in grid.batteries:
        for house in grid.houses:
            battery.distances.append(helpers.distance(house, battery))


def pick(battery):
    closest_index = battery.distances.index(min(battery.distances))
    return closest_index


<<<<<<< HEAD
=======
def check_cap(battery, house):
    if battery.capacity_used() <= battery.capacity:
        return True


>>>>>>> a0bcedc520526e4b6b839f29f196ec29248fdc3e
def remove_house(grid, closest_index):
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST


def draw(grid):
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
