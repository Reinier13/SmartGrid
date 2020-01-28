import random
import math
import copy
import numpy as np
from decimal import Decimal
from code.classes import tree
from code.helpers import distance

def simanneal(grid):
    """
    Simulated Annealing algorithm based on a Hill climb swap where houses swap
    batteries. Each improvement is approved and also sometimes it accepts
    solutions that are worse in hope for a better solution later on.
    """
    temperature = 1000
    cooling_rate = 0.95

    count = 0
    for k in range(1000):
        temporary_temperature = temperature * (cooling_rate ** k)
        if temporary_temperature < 1.000001:
            temporary_temperature = 1.000001

        grid_last_cost = copy.deepcopy(grid)
        swap(grid, temporary_temperature)
        grid.draw()

        if k == 0:
            grid_min_cost = copy.deepcopy(grid)
        if grid.calculate_cost() < grid_min_cost.calculate_cost():
            grid_min_cost = copy.deepcopy(grid)

        if grid.calculate_cost() == grid_last_cost.calculate_cost():
            count += 1
        else:
            count = 0

        if count == 10:
            break


def swap(grid, temperature):
    """
    Swaps a house with a house in another battery if the the solution improves
    and sometimes when the the solution is worse.
    """
    swap_house_1 = random.choice(grid.houses)
    for battery in grid.batteries:
        if swap_house_1 in battery.houses:
            swap_battery_1 = battery
            break

    swap_battery_2 = choose_battery(grid)
    while swap_battery_2 == swap_battery_1:
        swap_battery_2 = choose_battery(grid)

    for house in swap_battery_2.houses:
        swap_house_2 = house
        old_distance = distance(swap_house_1, swap_battery_1) + distance(swap_house_2, swap_battery_2)
        new_distance = distance(swap_house_2, swap_battery_1) + distance(swap_house_1, swap_battery_2)
        delta_distance = new_distance - old_distance

        if delta_distance < 0 and capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
            house_swap(swap_house_1, swap_house_2,swap_battery_1, swap_battery_2)
            break

        elif math.exp(-delta_distance/temperature) > random.random() and \
            capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
            house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2)
            break


def house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    """
    Swaps house with a house in another battery.
    """
    swap_battery_1.add_house(swap_battery_2.houses.pop(swap_battery_2.houses.index(swap_house_2)))
    swap_battery_2.add_house(swap_battery_1.houses.pop(swap_battery_1.houses.index(swap_house_1)))


def capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    """
    Checks if the capacity of both batteries is not exceeded.
    """
    capacity_1 = swap_battery_1.capacity_used() - swap_house_1.output + swap_house_2.output
    capacity_2 = swap_battery_2.capacity_used() - swap_house_2.output + swap_house_1.output
    if capacity_1 < swap_battery_1.capacity and capacity_2 < swap_battery_2.capacity:
        return True


def choose_battery(grid):
    """
    Chooses random battery.
    """
    other_battery = random.choice(grid.batteries)
    return other_battery
