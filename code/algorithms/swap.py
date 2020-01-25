import random
from .helpers import distance, draw, clear
from code.classes import tree

def hill_climb(grid):
    # create list to store improved grid costs
    costs = []

    # create counter to store number of identical cost outputs
    count = 0

    # iterate over desired number of improverments
    for i in range(30000):
        swap(grid)
        costs.append(grid.calculate_cost())

        # check identical cost outputs
        if costs[i] == costs[i-1]:
            count += 1
            if count == 1000:
                break
        else:
            count = 0

    draw(grid)

def swap(grid):

    # take random house and the battery that it's connected to
    swap_house_1 = random.choice(grid.houses)
    for battery in grid.batteries:
        if swap_house_1 in battery.houses:
            swap_battery_1 = battery
            break

    # get random battery not connected to house
    swap_battery_2 = choose_battery(grid)
    while swap_battery_2 == swap_battery_1:
        swap_battery_2 = choose_battery(grid)

    # iterate over all houses of random battery
    # which is not the battery that house 1 is connected to
    for house in swap_battery_2.houses:
        swap_house_2 = house

        # calculate distances
        old_distance = distance(swap_house_1, swap_battery_1) + distance(swap_house_2, swap_battery_2)
        new_distance = distance(swap_house_2, swap_battery_1) + distance(swap_house_1, swap_battery_2)

        # check if distance is improved and fits the capacity
        if new_distance < old_distance and capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):

            # swap the houses
            house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2)
            break


def house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    swap_battery_1.houses.append(swap_battery_2.houses.pop(swap_battery_2.houses.index(swap_house_2)))
    swap_battery_2.houses.append(swap_battery_1.houses.pop(swap_battery_1.houses.index(swap_house_1)))


def capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    capacity_1 = swap_battery_1.capacity_used() - swap_house_1.output + swap_house_2.output
    capacity_2 = swap_battery_2.capacity_used() - swap_house_2.output + swap_house_1.output
    if capacity_1 < swap_battery_1.capacity and capacity_2 < swap_battery_2.capacity:
        return True


def choose_battery(grid):
    other_battery = random.choice(grid.batteries)
    return other_battery
