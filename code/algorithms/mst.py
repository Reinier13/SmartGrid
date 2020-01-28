import random
from code.classes import node, tree
from code.classes.grid import Grid
from code.helpers import distance

def mst(grid):
    grid.trees = []
    for battery in grid.batteries:
        battery.tree = tree.Tree()
        battery.nodes = []
        battery.nodes.append(node.Node(battery.x, battery.y))
        for house in battery.houses:
            house.node = node.Node(house.x, house.y)
            closest_node = house.node.get_closest_node(battery.nodes)
            house.nodes = battery.tree.add_branch(house.node, closest_node)
            for node_obj in house.nodes:
                battery.nodes.append(node_obj)
        print(grid.calculate_cost())
        optimize(battery, battery.nodes, battery.tree)
        grid.trees.append(battery.tree)
    # swap(grid)


def optimize(battery, nodes, tree_obj):
    for i in range(10):
        house = random.choice(battery.houses)
        for node in house.nodes:
            nodes.remove(node)
        # nodes.remove(house.node)
        house.nodes = []
        closest_node = house.node.get_closest_node(nodes)
        # print(closest_node)
        house.nodes = tree_obj.add_branch(house.node, closest_node)
        for node_obj in house.nodes:
            nodes.append(node_obj)


def swap(grid):
    for i in range(300):
        rand_battery_1 = random.choice(grid.batteries)
        rand_battery_2 = random.choice(grid.batteries)

        # print("voor swap:", len(rand_battery_1.nodes))

        while rand_battery_1 == rand_battery_2:
            rand_battery_2 = random.choice(grid.batteries)

        rand_house_1 = random.choice(rand_battery_1.houses)
        rand_house_2 = random.choice(rand_battery_2.houses)

        old_distance = len(rand_house_1.nodes) + len(rand_house_2.nodes) - 2

        for node in rand_house_1.nodes:
            rand_battery_1.nodes.remove(node)

        for node in rand_house_2.nodes:
            rand_battery_2.nodes.remove(node)

        closest_node_1 = rand_house_1.node.get_closest_node(rand_battery_2.nodes)
        closest_node_1_dist = distance(rand_house_1, closest_node_1)

        closest_node_2 = rand_house_2.node.get_closest_node(rand_battery_1.nodes)
        closest_node_2_dist = distance(rand_house_2, closest_node_2)

        new_distance = closest_node_1_dist + closest_node_2_dist

        # print(old_distance)
        # print(new_distance)

        print('eeen....')
        if (new_distance < old_distance) and capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):
            print('JA!')

            rand_battery_1.add_house(rand_battery_2.houses.pop(rand_battery_2.houses.index(rand_house_2)))
            rand_battery_2.add_house(rand_battery_1.houses.pop(rand_battery_1.houses.index(rand_house_1)))

            rand_house_1.nodes = rand_battery_2.tree.add_branch(rand_house_1, closest_node_1)
            rand_house_2.nodes = rand_battery_1.tree.add_branch(rand_house_2, closest_node_2)


            for node_obj in rand_house_2.nodes:
                rand_battery_1.nodes.append(node_obj)

            for node_obj in rand_house_1.nodes:
                rand_battery_2.nodes.append(node_obj)
        else:
            for node_obj in rand_house_1.nodes:
                rand_battery_1.nodes.append(node_obj)

            for node_obj in rand_house_2.nodes:
                rand_battery_2.nodes.append(node_obj)

            # for tree_list in rand_battery_2.tree.branches:
            #     for node_obj in tree_list:
            #         rand_battery_2.nodes.append(node_obj)

def capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):
    capacity_1 = rand_battery_1.capacity_used() - rand_house_1.output + rand_house_1.output
    capacity_2 = rand_battery_2.capacity_used() - rand_house_1.output + rand_house_1.output

    if capacity_1 <= rand_battery_1.capacity and capacity_2 <= rand_battery_2.capacity:
        return True
