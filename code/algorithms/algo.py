import random
import numpy as np

def greedy(grid):
    for house in grid.houses:
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))

      closest = house.distances.index(min(house.distances))
    house.battery = grid.batteries[closest]

    # counter = 0

    if (house.battery.capacity_used() + house.output) < house.battery.capacity:
        array = np.array(house.distances)
        closest = house.distances.index(np.partition(array, 1)[1])

        battery.add_house(house)
        house.battery = grid.batteries[closest]
        house.add_cable()

        # counter += 1

    print(house.battery)


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
