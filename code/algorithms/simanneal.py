import random, math

def simanneal(grid):

    temperature = 10000
    cooling_rate = 0,95

    for i in range(1000):
        temperature_temporary = temperature / (i + 1)
        cost_old = grid.calculate_cost()
        print(temperature_temporary)
        swap(grid, temperature_temporary)

        # recable the houses
        for house in grid.houses:
            house.cables = []
            house.add_cable()


def swap(grid, temperature):
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
                delta_distance = old_distance - new_distance
                # check if distance is improved and fits the capacity
                if delta_distance > 0 and capacity_fit(swap_house_1, swap_house_2):

                    # swap the houses
                    house_swap(swap_house_1, swap_house_2, swap_battery)

                elif math.exp(delta_distance/temperature) > random.uniform(0,1):
                    house_swap(swap_house_1, swap_house_2, swap_battery)



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
