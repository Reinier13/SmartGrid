import random, math

def greedy(grid):
    num_houses = 0
    for house in grid.houses:
        for battery in grid.batteries:
            delta_x = house.x - battery.x
            delta_y = house.y - battery.y
            delta = delta_x + delta_y

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
        greedy(grid)
