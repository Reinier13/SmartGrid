import random
import numpy as np
# import sys
# sys.setrecursionlimit(15000)


def greedy(grid):
    random.shuffle(grid.batteries)
    for battery in grid.batteries:
        global counter
        counter = 0
        for house in grid.houses:
            battery.distances.append(distance(house, battery))

        assigned = 0
        assigned += len(battery.houses)

        while assigned < 30 and battery.capacity_used() < battery.capacity:
            find_houses(battery, grid.houses, grid)


def find_houses(battery, houses, grid):
    global counter

    distances = np.array(battery.distances)
    closest = battery.distances.index(np.partition(distances, counter)[counter])

    house = houses[closest]
    battery.add_house(house)
    house.battery = battery
    house.add_cable()

    if counter < 149:
        counter += 1


    # if battery.capacity_used() >= battery.capacity:
    #     if counter == 149:
    #         for battery in grid.batteries:
    #             battery.houses = []
    #         for house in houses:
    #             house.battery = None
    #             house.cables = []
    #         greedy(grid)
    #     house.cables = []
    #     battery.houses.remove(house)
    #     house.battery = None
    #     find_houses(battery, houses, grid)
    # find_houses(battery, houses, grid)


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
