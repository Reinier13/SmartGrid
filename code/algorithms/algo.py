import random
import numpy as np
# import sys
# sys.setrecursionlimit(15000)


def greedy(grid):
    random.shuffle(grid.houses)
    for house in grid.houses:
        global counter
        counter = 0
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))
        find_battery(house, grid.batteries, grid)


def find_battery(house, batteries, grid):
    global counter

    distances = np.array(house.distances)
    closest = house.distances.index(np.partition(distances, counter)[counter])

    house.battery = batteries[closest]
    house.battery.add_house(house)
    house.add_cable()

<<<<<<< HEAD
    if house.battery.capacity_used() >= house.battery.capacity:
=======
    if house.battery.capacity_used() >= battery.capacity:
>>>>>>> 8a58feffd7a1d8ce2784bc94bac6b0bb8959ab35
        if counter < 4:
            counter += 1
        if counter == 4:
            for battery in batteries:
                battery.houses = []
            for house in grid.houses:
                house.battery = None
                house.cables = []
            greedy(grid)
        house.cables = []
        house.battery.houses.remove(house)
        house.battery = None
        find_battery(house, batteries, grid)


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
