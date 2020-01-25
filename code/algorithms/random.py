import random
from code.classes import tree


def rand(grid):
    num_houses = 0
    random.shuffle(grid.houses)
    for battery in grid.batteries:
        tree_obj = tree.Tree()
        for house in grid.houses:
            capacity_used = battery.capacity_used()
            if battery.capacity > (capacity_used + house.output) and house.battery == None:
                battery.add_house(house)
                house.battery = battery
                tree_obj.add_nodes(house, battery)
        num_houses += len(battery.houses)
        grid.trees.append(tree_obj.nodes)

    if num_houses != len(grid.houses):
        for battery in grid.batteries:
            battery.houses = []
            tree_obj.nodes = []
        for house in grid.houses:
            house.battery = None
        grid.trees = []
        rand(grid)
