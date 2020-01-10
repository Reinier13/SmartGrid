import random

def greedy(grid):
    for battery in grid.batteries:
        cap = battery.capacity
        for house in grid.houses:
            used_capacity = battery.capacity_used()
            if cap > (used_capacity + house.output) and house.connected == False:
                battery.add_house(house)
                house.connected = True
