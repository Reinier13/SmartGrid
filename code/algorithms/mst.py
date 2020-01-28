import random
from code.classes import node, tree
from code.classes.grid import Grid
from code.helpers import distance


def mst(grid):
    """
    Create nodes for all batteries and houses and let (in order of increasing
    distance) houses pick their nearest node and connect to it, resulting in a
    minimum spanning tree based on Prims algorithm.
    """
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
        optimize(battery, battery.nodes, battery.tree)
    # swap(grid)
    for battery in grid.batteries:
        grid.trees.append(battery.tree)


def optimize(battery, nodes, tree_obj):
    for i in range(100):
        house = random.choice(battery.houses)
        for node in house.nodes:
            nodes.remove(node)
        nodes.remove(house.node)
        house.nodes = []
        closest_node = house.node.get_closest_node(nodes)
        house.nodes = tree_obj.add_branch(house.node, closest_node)
        for branch in tree_obj.branches:
            for node_obj in branch:
                nodes.append(node_obj)


def swap(grid):
    for i in range(10000):
        rand_battery_1 = random.choice(grid.batteries)
        rand_battery_2 = random.choice(grid.batteries)

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

        if new_distance < old_distance and capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):
            perform_swap(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2, closest_node_1, closest_node_2)

        else:
            for node_obj in rand_house_1.nodes:
                rand_battery_1.nodes.append(node_obj)

            for node_obj in rand_house_2.nodes:
                rand_battery_2.nodes.append(node_obj)


def perform_swap(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2, closest_node_1, closest_node_2):
    rand_battery_1.tree.branches.pop(rand_battery_1.houses.index(rand_house_1))
    rand_battery_2.tree.branches.pop(rand_battery_2.houses.index(rand_house_2))

    rand_battery_1.add_house(rand_battery_2.houses.pop(rand_battery_2.houses.index(rand_house_2)))
    rand_battery_2.add_house(rand_battery_1.houses.pop(rand_battery_1.houses.index(rand_house_1)))

    rand_house_1.nodes = rand_battery_2.tree.add_branch(rand_house_1, closest_node_1)
    rand_house_2.nodes = rand_battery_1.tree.add_branch(rand_house_2, closest_node_2)

    for node_obj in rand_house_2.nodes:
        rand_battery_1.nodes.append(node_obj)

    for node_obj in rand_house_1.nodes:
        rand_battery_2.nodes.append(node_obj)


def capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):
    capacity_1 = rand_battery_1.capacity_used() - rand_house_1.output + rand_house_1.output
    capacity_2 = rand_battery_2.capacity_used() - rand_house_1.output + rand_house_1.output

    if capacity_1 <= rand_battery_1.capacity and capacity_2 <= rand_battery_2.capacity:
        return True
