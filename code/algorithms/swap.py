import random

def hill_climb(grid):
<<<<<<< HEAD

=======
    for i in range(1000):
        swap(grid)
>>>>>>> b346ed088ba27f6c1b149daac05a01fa78961d6a

def swap(grid):
    swap_house_1 = random.choice(grid.houses)
    swap_battery = choose_battery(grid)

    while swap_battery == swap_house_1.battery:
        swap_battery = choose_battery(grid)

    swap_house_2 = random.choice(swap_battery.houses)

    old_distance = distance(swap_house_1, swap_house_1.battery) + distance(swap_house_2, swap_house_2.battery)
    new_distance = distance(swap_house_2, swap_house_1.battery) + distance(swap_house_1, swap_house_2.battery)

    if new_distance < old_distance and capacity_fit(swap_house_1, swap_house_2):
        print('LOOP')
        swap_house_2.battery = swap_house_1.battery
        swap_house_1.battery = swap_battery


def capacity_fit(swap_house_1, swap_house_2):
    capacity_1 = swap_house_1.battery.capacity_used() - swap_house_1.output + swap_house_2.output
    capacity_2 = swap_house_2.battery.capacity_used() - swap_house_2.output + swap_house_1.output
    if capacity_1 < swap_house_1.battery.capacity and capacity_2 < swap_house_2.battery.capacity:
        return True


def choose_battery(grid):
<<<<<<< HEAD
    battery = random.choice(grid.batteries)
    return battery
=======
    other_battery = random.choice(grid.batteries)
    return other_battery


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
>>>>>>> b346ed088ba27f6c1b149daac05a01fa78961d6a
