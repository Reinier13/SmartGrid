import random
from code.algorithms.helpers import distance

def hillclimb(grid, num_houses):
        costs = []
        count = 0
        for i in range(200000):
            multiple_swap(grid, num_houses)
            costs.append(grid.calculate_cost())
            if costs[i] == costs[i-1]:
                count += 1
                if count == 15000:
                    break
            else:
                count = 0
        grid.draw()



def multiple_swap(grid, num_houses):
    swap_battery_1 = choose_battery(grid)
    swap_houses_1 = []
    for i in range(num_houses):
        swap_house_1 = random.choice(swap_battery_1.houses)
        while swap_house_1 in swap_houses_1:
            swap_house_1 = random.choice(swap_battery_1.houses)
        swap_houses_1.append(swap_house_1)

    swap_battery_2 = choose_battery(grid)
    while swap_battery_1 == swap_battery_2:
        swap_battery_2 = choose_battery(grid)

    swap_houses_2 = []
    for i in range(num_houses):
        swap_house_2 = random.choice(swap_battery_2.houses)
        while swap_house_2 in swap_houses_2:
            swap_house_2 = random.choice(swap_battery_2.houses)
        swap_houses_2.append(swap_house_2)

    # calculate distances
    old_distance = 0
    new_distance = 0

    for house in swap_houses_1:
        old_distance += distance(house, swap_battery_1)
        new_distance += distance(house, swap_battery_2)

    for house in swap_houses_2:
        old_distance += distance(house, swap_battery_2)
        new_distance += distance(house, swap_battery_1)

    # check if distance is improved and fits the capacity
    if new_distance < old_distance and capacity_fit(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2):

        # swap the houses
        houses_swap(swap_houses_1, swap_houses_2,swap_battery_1, swap_battery_2, num_houses)


def houses_swap(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2, num_houses):
    for i in range(num_houses):
        house_1 = swap_houses_1[i]
        house_2 = swap_houses_2[i]

        swap_battery_1.houses.append(swap_battery_2.houses.pop(swap_battery_2.houses.index(house_2)))
        swap_battery_2.houses.append(swap_battery_1.houses.pop(swap_battery_1.houses.index(house_1)))


def choose_battery(grid):
    other_battery = random.choice(grid.batteries)
    return other_battery


def capacity_fit(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2):
    output_1 = 0
    output_2 = 0

    for house in swap_houses_1:
        output_1 += house.output

    for house in swap_houses_2:
        output_2 += house.output

    capacity_1 = swap_battery_1.capacity_used() - output_1 + output_2
    capacity_2 = swap_battery_2.capacity_used() - output_2 + output_1

    if capacity_1 < swap_battery_1.capacity and capacity_2 < swap_battery_2.capacity:
        return True
