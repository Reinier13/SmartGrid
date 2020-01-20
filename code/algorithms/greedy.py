import random
import numpy as np


MAX_DIST = 10000

def greedy(grid):
    create_distances(grid)
    for battery in grid.batteries:
        while check_cap(battery):
            closest_index = pick(battery)
            remove_house(grid, closest_index)
            battery.houses.append(grid.houses[closest_index])
            
    draw(grid)

# def draft(grid):
#     create_distances(grid)
#     house_available = True
#     while house_available:
#         for battery in grid.batteries:
#             closest_index = pick(battery)
#             if check_cap(battery):
#                 if battery.distances[closest_index] == MAX_DIST:
#                     house_available = False
#                     break
#
#                 remove_house(grid, closest_index)
#                 battery.houses.append(grid.houses[closest_index])
#     draw(grid)


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


def check_cap(battery):
    if battery.capacity_used() <= battery.capacity:
        return True


def remove_house(grid, closest_index):
    for battery in grid.batteries:
        battery.distances[closest_index] = MAX_DIST


def draw(grid):
    for battery in grid.batteries:
        for house in battery.houses:
            house.battery = battery
            house.add_cable()
