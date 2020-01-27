import random
from code.classes import tree


def rand(grid):
    num_houses = 0
    random.shuffle(grid.houses)
    for battery in grid.batteries:
        for house in grid.houses:
            capacity_used = battery.capacity_used()
            if (battery.capacity > (capacity_used + house.output)) and house.battery == None:
                battery.add_house(house)
                house.battery = battery
        num_houses += len(battery.houses)

    if num_houses != len(grid.houses):
        grid.clear()
        rand(grid)
    else:
        grid.draw()

