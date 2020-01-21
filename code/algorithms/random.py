import random


def rand(grid):
    for battery in grid.batteries:
        battery.houses = []
    for house in grid.houses:
        house.battery = None
        house.cables = []

    num_houses = 0
    random.shuffle(grid.houses)
    for battery in grid.batteries:
        for house in grid.houses:
            capacity_used = battery.capacity_used()
            if battery.capacity > (capacity_used + house.output) and house.battery == None:
                battery.add_house(house)
                house.battery = battery
                house.add_cable()
        num_houses += len(battery.houses)

    if num_houses != len(grid.houses):
        for battery in grid.batteries:
            battery.houses = []
        for house in grid.houses:
            house.battery = None
            house.cables = []
        rand(grid)
