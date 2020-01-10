import random

def greedy(grid):
    for battery in grid.batteries:
        cap = battery.capacity
        for house in grid.houses:
            if cap > float(battery.capacity_used) and house.connected == False:
                battery.add_house(house)
                house.connected = True
