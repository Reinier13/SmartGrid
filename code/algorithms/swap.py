import random

def hill_climb(grid):
    # create list to store improved grid costs
    costs = []

    # iterate over desired number of improverments
    for i in range(80):
        swap(grid)
        costs.append(grid.calculate_cost())

        # testing print statement
        print(costs[i-1])

        # break if the improvements don't exceed 10
        if i > 1 and costs[i] > costs[i-1] - 10:
            break

    # test print the number of iterations performed
    print(i)

def swap(grid):
    # boolean true until cost is decreased
    NoLowerCost = True

    while NoLowerCost:
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
                for house in swap_battery.houses:
                    swap_house_2 = house

                    # calculate distances
                    old_distance = distance(swap_house_1, swap_house_1.battery) + distance(swap_house_2, swap_house_2.battery)
                    new_distance = distance(swap_house_2, swap_house_1.battery) + distance(swap_house_1, swap_house_2.battery)

                    # check if distance is improved and fits the capacity
                    if new_distance < old_distance and capacity_fit(swap_house_1, swap_house_2):

                        # swap the houses
                        house_swap(swap_house_1, swap_house_2, swap_battery)

                        # recable the houses
                        for house in grid.houses:
                            house.cables = []
                            house.add_cable()

                        # lower cost is found
                        NoLowerCost = False


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


def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
