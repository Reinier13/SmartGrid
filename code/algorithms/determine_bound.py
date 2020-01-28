import random
import numpy as np
from code.helpers import distance


def connect_nocap(grid):
    random.shuffle(grid.houses)
    for house in grid.houses:
        global counter
        # to find the closest battery
        counter = 0
        # to find the furthest battery
        # counter = 4
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))
        find_battery(house, grid.batteries, grid)
    grid.draw()


def find_battery(house, batteries, grid):
    global counter
    distances = np.array(house.distances)
    closest = house.distances.index(np.partition(distances, counter)[counter])

    house.battery = batteries[closest]
    house.battery.add_house(house)
