import random
import numpy as np
from .mst import mst
from code.algorithms.helpers import distance


MAX_DIST = 10000

def greedy(grid):
    """
    Greedy algorithm that chooses a random battery and connects with houses
    that are closest until the capacity of the battery is reached.
    """
    grid.clear()
    random.shuffle(grid.batteries)
    create_distances(grid)
    for battery in grid.batteries:
        closest_house_index = pick(battery)

        # keep making connections until capacity is reached
        while battery.check_cap():

            # get index of closest house to battery
            closest_house_index = pick(battery)
            if battery.distances[closest_house_index] == MAX_DIST:
                break
            battery.houses.append(grid.houses[closest_house_index])
            remove_house(grid, closest_house_index)
    fit(grid)


def draft(grid):
    """
    Draft - Greedy algorithm that connects the batteries in turn with the houses
    that are closest to that battery until the capacity of the battery is
    reached.
    """
    grid.clear()
    random.shuffle(grid.batteries)
    create_distances(grid)
    house_available = True
    while house_available:
        for battery in grid.batteries:
            closest_house_index = pick(battery)
            if battery.check_cap():
                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break
                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
    fit(grid)


def fit(grid):
    count = 0
    while check_houses_cap(grid) == False:
        arrange(grid, count)
        count += 1
        if count == 25:
            greedy(grid)
    grid.draw()


def arrange(grid, count):
    capacities_used = []
    for battery in grid.batteries:
        capacities_used.append(battery.capacity_used())
        bat_max_cap_index = capacities_used.index(max(capacities_used))
        bat_min_cap_index = capacities_used.index(min(capacities_used))
        bat_max_cap = grid.batteries[bat_max_cap_index]
        bat_min_cap = grid.batteries[bat_min_cap_index]

    bat_max_cap.distances = []
    for house in bat_max_cap.houses:
        bat_max_cap.distances.append(distance(house, bat_max_cap))

    array = np.array(bat_max_cap.distances)
    bat_max_dist_index = bat_max_cap.distances.index(np.partition(array, -(count+1))[-(count+1)])
    max_dist = bat_max_cap.houses[bat_max_dist_index]

    bat_min_cap.houses.append(bat_max_cap.houses.pop(bat_max_dist_index))


def check_houses_cap(grid):
    """
    Check if all houses are compliant to the capacity constraint. Return False
    if this is not the case.
    """
    count = 0
    for battery in grid.batteries:
        if battery.check_cap():
            count += 1
    if count != len(grid.batteries):
        return False


def create_distances(grid):
    """
    Creates distances for all batteries from the battery to all its houses.
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
    Marks house as connected to a battery by setting the distance to a max.
    """
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST
