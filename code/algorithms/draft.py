import random
import numpy as np


MAX_DIST = 10000


def draft(grid):
    clear(grid)
    num_houses = 0
    random.shuffle(grid.batteries)

    create_distances(grid)

    house_available = True
    while house_available:

        for battery in grid.batteries:
            closest_house_index = pick(battery)
            if check_cap(battery):

                if battery.distances[closest_house_index] == MAX_DIST:
                    house_available = False
                    break

                remove_house(grid, closest_house_index)
                battery.houses.append(grid.houses[closest_house_index])
                num_houses += 1
    print(num_houses)
    print(grid.batteries[4].capacity_used())

    if num_houses < len(grid.houses):
        draft(grid)
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
    closest_house_index = battery.distances.index(min(battery.distances))
    return closest_house_index


def check_cap(battery):
    if battery.capacity_used() <= battery.capacity:
        return True


def remove_house(grid, closest_house_index):
    for battery in grid.batteries:
        battery.distances[closest_house_index] = MAX_DIST


def draw(grid):
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
