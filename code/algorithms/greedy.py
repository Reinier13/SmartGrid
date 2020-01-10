import random

def greedy(grid):
    num_houses = 0
    random.shuffle(grid.houses)
    # shuffled = random.sample(grid.houses, len(grid.houses))
    for battery in grid.batteries:
        cap = battery.capacity
        for house in grid.houses:
            used_capacity = battery.capacity_used()
            if cap > (used_capacity + house.output) and house.connected == False:
                battery.add_house(house)
                house.connected = True
                house.battery = battery
        num_houses += len(battery.houses)
    print(num_houses)

    # if num_houses != len(grid.houses):
    #     for house in grid.houses:
    #         house.connected = False
    #     greedy(grid)

    # K-HOLE PROBLEEM!!! ALS NIET IN 1 KEER GOED, DAN SHUFFLED LIJST ELKE KEER ZELFDE VOLGORDE
