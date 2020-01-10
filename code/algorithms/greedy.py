import random

def greedy(grid):
    num_houses = 0
    random.shuffle(grid.houses)
    for battery in grid.batteries:
        cap = battery.capacity
        for house in grid.houses:
            used_capacity = battery.capacity_used()
            if cap > (used_capacity + house.output) and house.connected == False:
                battery.add_house(house)
                house.connected = True
        num_houses += len(battery.houses)
        print(num_houses)
    if num_houses != len(grid.houses):
        greedy(grid)
