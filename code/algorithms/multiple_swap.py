import random

def hill_climb(grid, num_houses):
    # create list to store improved grid costs
    costs = []

    # create counter to store number of identical cost outputs
    count = 0

    # iterate over desired number of improverments
    for i in range(30000):
        multiple_swap(grid, num_houses)
        costs.append(grid.calculate_cost())

        # check identical cost outputs
        if costs[i] == costs[i-1]:
            count += 1
            if count == 1000:
                break
        else:
            count = 0

    for house in grid.houses:
        grid.trees.append(house.cables)


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
    if new_distance < old_distance and capacity_fit(swap_houses_1, swap_houses_2):

        # swap the houses
        houses_swap(swap_houses_1, swap_houses_2, swap_battery_2, num_houses)

        print(1)

        # recable the houses
        for house in grid.houses:
            house.cables = []
            house.add_cable()


def houses_swap(swap_houses_1, swap_houses_2, swap_battery_2, num_houses):
    for i in range(num_houses):
        house_1 = swap_houses_1[i]
        house_2 = swap_houses_2[i]
<<<<<<< HEAD

=======
>>>>>>> 2cd3511d77dd4dca48c7a76851404fcbfa275dd9
        house_1.battery.houses.append(house_2.battery.houses.pop(house_2.battery.houses.index(house_2)))
        house_2.battery.houses.append(house_1.battery.houses.pop(house_1.battery.houses.index(house_1)))
        house_2.battery = house_1.battery
        house_1.battery = swap_battery_2


def choose_battery(grid):
    other_battery = random.choice(grid.batteries)
    return other_battery


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta

def capacity_fit(swap_houses_1, swap_houses_2):
    output_1 = 0
    output_2 = 0

    for house in swap_houses_1:
        output_1 += house.output

    for house in swap_houses_2:
        output_2 += house.output

    capacity_1 = swap_houses_1[0].battery.capacity_used() - output_1 + output_2
    capacity_2 = swap_houses_2[0].battery.capacity_used() - output_2 + output_1

    if capacity_1 < swap_houses_1[0].battery.capacity and capacity_2 < swap_houses_2[0].battery.capacity:
        return True
