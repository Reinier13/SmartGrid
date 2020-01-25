import random
import numpy as np
from code.algorithms.helpers import distance, draw, clear


MAX_DIST = 10000


def draft(grid):
    """
    Draft - Greedy algorithm that connects the batteries in turn with the houses
    that are closest to that battery until the capacity of the battery is
    reached.
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
            if battery.check_cap():

                # end algorithm if all houses are connected
                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break

                # connect house to battery and mark as connected
                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
                num_houses += 1

    count = 0
    while check_houses_cap(grid) == False:
        arrange(grid, count)
        count += 1
        if count == 25:
            draft(grid)
    draw(grid)


def arrange(grid, count):
    capacities_used = []
    for battery in grid.batteries:
        capacities_used.append(battery.capacity_used())
        max_index = capacities_used.index(max(capacities_used))
        min_index = capacities_used.index(min(capacities_used))
        max_cap = grid.batteries[max_index]
        min_cap = grid.batteries[min_index]

    max_cap.distances = []
    for house in max_cap.houses:
        max_cap.distances.append(distance(house, max_cap))

    array = np.array(max_cap.distances)
    max_dist_index = max_cap.distances.index(np.partition(array, -(count+1))[-(count+1)])
    max_dist = max_cap.houses[max_dist_index]

    min_cap.houses.append(max_cap.houses.pop(max_dist_index))

def check_houses_cap(grid):
    count = 0
    for battery in grid.batteries:
        if battery.check_cap():
            count += 1
    if count != len(grid.batteries):
        return False


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
