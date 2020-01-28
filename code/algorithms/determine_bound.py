import random
import numpy as np
from code.algorithms.helpers import distance


def greedy(grid):
    random.shuffle(grid.houses)
    for house in grid.houses:
        global counter
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))
        find_battery(house, grid.batteries, grid)
    grid.draw()


def find_battery(house, batteries, grid):
    distances = np.array(house.distances)
    closest = house.distances.index(np.partition(distances, counter)[counter])

    house.battery = batteries[closest]
    house.battery.add_house(house)