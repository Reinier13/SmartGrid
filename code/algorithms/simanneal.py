import random
import math
import copy

from code.classes import tree

def simanneal(grid):
    """
    Simulated Annealing algorithm based on a Hill climb swap where houses swap
    batteries. Each improvement is approved and also sometimes it accepts
    solutions that are worse in hope for a better solution later on.
    """
    temperature = 10000
    cooling_rate = 0.99
    count = 0
    for i in range(1000):

        # exponential cooling scheme
        temporary_temperature = temperature * (cooling_rate ** i)
        if temporary_temperature < 1.000001:
            temporary_temperature = 1.000001

        # temporary_temperature = temperature - (cooling_rate * i)

        grid_last_cost = copy.deepcopy(grid)
        swap(grid, temporary_temperature)

        grid.draw()

        if i == 0:
            grid_min_cost = copy.deepcopy(grid)



        if grid.calculate_cost() < grid_min_cost.calculate_cost():
            grid_min_cost = copy.deepcopy(grid)
        print(grid_min_cost.calculate_cost())


        if grid.calculate_cost() == grid_last_cost.calculate_cost():
            count += 1
            print(count)
            if count == 10:
                break
        else:
            count = 0


    return grid_min_cost

def swap(grid, temperature):
    """
    Swaps a house with a house in another battery if the the solution improves
    and sometimes when the the solution is worse.
    """

    # take random house and battery it is connected to
    swap_house_1 = random.choice(grid.houses)
    for battery in grid.batteries:
        if swap_house_1 in battery.houses:
            swap_battery_1 = battery
            break


    # make sure house and battery aren't connected
    swap_battery_2 = choose_battery(grid)
    while swap_battery_2 == swap_battery_1:
        swap_battery_2 = choose_battery(grid)

    # iterate over all houses of all batteries
    # expect the battery that house 1 is connected to

    for house in swap_battery_2.houses:
        swap_house_2 = house

        # calculate distances
        old_distance = distance(swap_house_1, swap_battery_1) + distance(swap_house_2, swap_battery_2)
        new_distance = distance(swap_house_2, swap_battery_1) + distance(swap_house_1, swap_battery_2)
        delta_distance = new_distance - old_distance

        # check if distance is improved and fits the capacity
        if delta_distance < 0 and capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):

            print('Improvement')

            # swap the houses
            house_swap(swap_house_1, swap_house_2,swap_battery_1, swap_battery_2)
            break

        # also do swap by random chance if not improved
        elif math.exp(-(delta_distance/temperature)) > random.random() and \
            capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):

            house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2)
            break



def house_swap(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    """
    Swaps house with a house in another battery.
    """
    swap_battery_1.houses.append(swap_battery_2.houses.pop(swap_battery_2.houses.index(swap_house_2)))
    swap_battery_2.houses.append(swap_battery_1.houses.pop(swap_battery_1.houses.index(swap_house_1)))


def capacity_fit(swap_house_1, swap_house_2, swap_battery_1, swap_battery_2):
    """
    Checks if the capacity is not exceeded.
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


def distance(house, battery):
    """
    Computes distance between house and battery.
    """
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
