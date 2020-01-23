def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta

def calculate_cost2(grid, trees):
    cost = 0
    for battery in grid.batteries:
        cost += battery.cost
    for tree in trees:
        for branch in tree:
            # print(branch)
            cost += ((len(branch) - 1) * 9)
    return cost
