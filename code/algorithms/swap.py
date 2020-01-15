import random

def hill_climb(grid):


def swap(grid):
    swap_house = random.choice(grid.houses)
    new_battery = choose_battery(grid)

    while new_battery == swap_house.battery:
        new_battery = choose_battery(grid)

    swapped_house = random.choice(new_battery.houses)
    swapped_house.battery = swap_house.battery
    swap_house.battery = new_battery


def choose_battery(grid):
    battery = random.choice(grid.batteries)
    return battery
