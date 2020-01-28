import random
from code.helpers import distance

def hill_climb(grid, num_houses):
    costs = []
    count = 0
    for i in range(200000):
        multiple_swap(grid, num_houses)
        costs.append(grid.calculate_cost())
        if costs[i] == costs[i-1]:
            count += 1
            if count == 20000:
                break
        else:
            count = 0
    grid.draw()


def multiple_swap(grid, num_houses):
    swap_battery_1 = random.choice(grid.batteries)
    swap_battery_2 = random.choice(grid.batteries)
    swap_houses_1 = []
    swap_houses_2 = []

    while swap_battery_1 == swap_battery_2:
        swap_battery_2 = random.choice(grid.batteries)

    for i in range(num_houses):
        swap_house_1 = random.choice(swap_battery_1.houses)
        while swap_house_1 in swap_houses_1:
            swap_house_1 = random.choice(swap_battery_1.houses)
        swap_houses_1.append(swap_house_1)

        swap_house_2 = random.choice(swap_battery_2.houses)
        while swap_house_2 in swap_houses_2:
            swap_house_2 = random.choice(swap_battery_2.houses)
        swap_houses_2.append(swap_house_2)

    old_distance, new_distance = 0, 0

    for house in swap_houses_1:
        old_distance += distance(house, swap_battery_1)
        new_distance += distance(house, swap_battery_2)

    for house in swap_houses_2:
        old_distance += distance(house, swap_battery_2)
        new_distance += distance(house, swap_battery_1)

    if new_distance < old_distance and capacity_fit(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2):
        houses_swap(swap_houses_1, swap_houses_2,swap_battery_1, swap_battery_2, num_houses)


def houses_swap(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2, num_houses):
    for i in range(num_houses):
        house_1 = swap_houses_1[i]
        house_2 = swap_houses_2[i]

        swap_battery_1.add_house(swap_battery_2.houses.pop(swap_battery_2.houses.index(house_2)))
        swap_battery_2.add_house(swap_battery_1.houses.pop(swap_battery_1.houses.index(house_1)))


def capacity_fit(swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2):
    output_1 = 0
    output_2 = 0

    for house in swap_houses_1:
        output_1 += house.output

    for house in swap_houses_2:
        output_2 += house.output

    capacity_1 = swap_battery_1.capacity_used() - output_1 + output_2
    capacity_2 = swap_battery_2.capacity_used() - output_2 + output_1

    if capacity_1 <= swap_battery_1.capacity and capacity_2 <= swap_battery_2.capacity:
        return True
