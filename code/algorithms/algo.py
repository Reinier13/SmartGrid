import random, math

def greedy(grid):
    num_houses = 0
    for battery in grid.batteries:
        for house in grid.houses:
            delta_x = house.x - battery.x
            delta_y = house.y - battery.y
            delta = delta_x + delta_y
