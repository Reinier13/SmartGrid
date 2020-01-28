import random
from code.classes import node, tree
from code.classes.grid import Grid
from code.algorithms.helpers import distance

def mst(grid):
    grid.trees = []
    for battery in grid.batteries:
        battery.tree = tree.Tree()
        battery.nodes = []
        battery.nodes.append(node.Node(battery.x, battery.y))
        for house in battery.houses:
            house.node = node.Node(house.x, house.y)
            closest_node = house.node.get_closest_node(battery.nodes)
            house.nodes = battery.tree.add_nodes(house.node, closest_node)
            for tree_list in battery.tree.nodes:
                for node_obj in tree_list:
                    battery.nodes.append(node_obj)
        # optimize(battery, battery.nodes, battery.tree)
    swap(grid)
    for battery in grid.batteries:
        grid.trees.append(battery.tree.nodes)


def optimize(battery, nodes, tree_obj):
    for i in range(5):
        house = random.choice(battery.houses)
        print(house.node)
        for node in house.nodes:
            nodes.remove(node)
        nodes.remove(house.node)
        house.nodes = []
        closest_node = house.node.get_closest_node(nodes)
        print(closest_node)
        house.nodes = tree_obj.add_nodes(house.node, closest_node)
        for tree_list in tree_obj.nodes:
            for node_obj in tree_list:
                nodes.append(node_obj)


def swap(grid):
    for i in range(500):
        rand_battery_1 = random.choice(grid.batteries)
        rand_battery_2 = random.choice(grid.batteries)

        while rand_battery_1 == rand_battery_2:
            rand_battery_2 = random.choice(grid.batteries)

        rand_house_1 = random.choice(rand_battery_1.houses)
        rand_house_2 = random.choice(rand_battery_2.houses)

        old_distance = len(rand_house_1.nodes) + len(rand_house_2.nodes) - 2
        print(old_distance)

        closest_node_1 = rand_house_1.node.get_closest_node(rand_battery_2.nodes)
        closest_node_1_dist = distance(rand_house_1, closest_node_1)
        closest_node_2 = rand_house_2.node.get_closest_node(rand_battery_1.nodes)
        closest_node_2_dist = distance(rand_house_2, closest_node_2)
        new_distance = closest_node_1_dist + closest_node_2_dist
        print(new_distance)

        if new_distance < old_distance:
            print('LiL SW4P!!11!!')

            for node in rand_house_1.nodes:
                rand_battery_1.nodes.remove(node)
            for node in rand_house_2.nodes:
                rand_battery_2.nodes.remove(node)

            rand_battery_1.add_house(rand_battery_2.houses.pop(rand_battery_2.houses.index(rand_house_2)))
            rand_battery_2.add_house(rand_battery_1.houses.pop(rand_battery_1.houses.index(rand_house_1)))

            rand_house_1.nodes = rand_battery_2.tree.add_nodes(rand_house_1, closest_node_1)
            rand_house_2.nodes = rand_battery_1.tree.add_nodes(rand_house_2, closest_node_2)

            for tree_list in rand_battery_1.tree.nodes:
                for node_obj in tree_list:
                    rand_battery_1.nodes.append(node_obj)

            for tree_list in rand_battery_2.tree.nodes:
                for node_obj in tree_list:
                    rand_battery_2.nodes.append(node_obj)
