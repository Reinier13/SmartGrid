import random
from .helpers import distance
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

    for battery in grid.batteries:
        tree_obj = tree.Tree()
        for house in battery.houses:
            tree_obj.add_nodes(house, battery)
        grid.trees.append(tree_obj.nodes)

def swap(grid):
    # take random house and battery
    swap_house_1 = random.choice(grid.houses)
    swap_battery = choose_battery(grid)

    # make sure house and battery aren't connected
    while swap_battery == swap_house_1.battery:
        swap_battery = choose_battery(grid)

    # iterate over all houses of all batteries
    # expect the battery that house 1 is connected to
    for swap_battery in grid.batteries:
        if swap_battery == swap_house_1.battery:
            continue
        else:
            # tree_obj = tree.Tree()
            for house in swap_battery.houses:
                swap_house_2 = house

                # calculate distances
                old_distance = distance(swap_house_1, swap_house_1.battery) + distance(swap_house_2, swap_house_2.battery)
                new_distance = distance(swap_house_2, swap_house_1.battery) + distance(swap_house_1, swap_house_2.battery)

                # check if distance is improved and fits the capacity
                if new_distance < old_distance and capacity_fit(swap_house_1, swap_house_2):

                    # swap the houses
                    house_swap(swap_house_1, swap_house_2, swap_battery)
                    print('SWAP!')


def house_swap(swap_house_1, swap_house_2, swap_battery):
    swap_house_1.battery.houses.append(swap_house_2.battery.houses.pop(swap_house_2.battery.houses.index(swap_house_2)))
    swap_house_2.battery.houses.append(swap_house_1.battery.houses.pop(swap_house_1.battery.houses.index(swap_house_1)))
    swap_house_2.battery = swap_house_1.battery
    swap_house_1.battery = swap_battery


def capacity_fit(swap_house_1, swap_house_2):
    capacity_1 = swap_house_1.battery.capacity_used() - swap_house_1.output + swap_house_2.output
    capacity_2 = swap_house_2.battery.capacity_used() - swap_house_2.output + swap_house_1.output
    if capacity_1 < swap_house_1.battery.capacity and capacity_2 < swap_house_2.battery.capacity:
        return True


def choose_battery(grid):
    other_battery = random.choice(grid.batteries)
    return other_battery
