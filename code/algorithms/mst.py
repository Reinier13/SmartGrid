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
            house.nodes = battery.tree.add_nodes(house.node, closest_node)
        for branch in battery.tree.nodes:
            for node_obj in branch:
                battery.nodes.append(node_obj)

        print(battery.nodes)
        break
        # optimize(battery, battery.nodes, battery.tree)
        grid.trees.append(battery.tree.nodes)
    print(grid.calculate_cost())
    swap(grid)
    grid.trees = []
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
    for i in range(100):
        rand_battery_1 = random.choice(grid.batteries)
        rand_battery_2 = random.choice(grid.batteries)

        print("voor swap:", len(rand_battery_1.nodes))

        while rand_battery_1 == rand_battery_2:
            rand_battery_2 = random.choice(grid.batteries)

        rand_house_1 = random.choice(rand_battery_1.houses)
        rand_house_2 = random.choice(rand_battery_2.houses)

        old_distance = len(rand_house_1.nodes) + len(rand_house_2.nodes)
        # print(old_distance)

        closest_node_1 = rand_house_1.node.get_closest_node(rand_battery_2.nodes)
        closest_node_1_dist = distance(rand_house_1, closest_node_1)

        closest_node_2 = rand_house_2.node.get_closest_node(rand_battery_1.nodes)
        closest_node_2_dist = distance(rand_house_2, closest_node_2)

        new_distance = closest_node_1_dist + closest_node_2_dist
        # print(new_distance)

        if new_distance < old_distance and capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):
            print('LiL SW4P!!11!!')
            # print(rand_battery_1.tree.nodes)

            # if rand_battery_1.nodes == rand_battery_1.tree.nodes:
            # print(rand_battery_1.tree.nodes)

            print(len(rand_battery_1.nodes))


            for node in rand_house_1.nodes:

                rand_battery_1.nodes.remove(node)

            for node in rand_house_2.nodes:
                rand_battery_2.nodes.remove(node)

            rand_battery_1.tree.nodes = []
            rand_battery_2.tree.nodes = []
            rand_battery_2.tree.nodes.append(rand_battery_2.nodes)
            rand_battery_1.tree.nodes.append(rand_battery_1.nodes)
            # if len(rand_battery_2.tree.nodes) != len(set(rand_battery_2.tree.nodes)):
            #     print('JA2')
            # else:
            #     print('Nee2')


            rand_battery_1.add_house(rand_battery_2.houses.pop(rand_battery_2.houses.index(rand_house_2)))
            rand_battery_2.add_house(rand_battery_1.houses.pop(rand_battery_1.houses.index(rand_house_1)))

            rand_house_1.nodes = rand_battery_2.tree.add_nodes(rand_house_1, closest_node_1)
            rand_house_2.nodes = rand_battery_1.tree.add_nodes(rand_house_2, closest_node_2)

            # if len(rand_battery_2.tree.nodes) != len(set(rand_battery_2.tree.nodes)):
            #
            #     print('JA')
            # else:
            #     print('Nee')
            rand_battery_1.nodes = []
            rand_battery_2.nodes = []

            for tree_list in rand_battery_1.tree.nodes:
                for node_obj in tree_list:
                    rand_battery_1.nodes.append(node_obj)
            print(len(rand_battery_1.nodes))

            for tree_list in rand_battery_2.tree.nodes:
                for node_obj in tree_list:
                    rand_battery_2.nodes.append(node_obj)


def capacity_fit(rand_house_1, rand_house_2, rand_battery_1, rand_battery_2):

    capacity_1 = rand_battery_1.capacity_used() - rand_house_1.output + rand_house_1.output
    capacity_2 = rand_battery_2.capacity_used() - rand_house_1.output + rand_house_1.output

    if capacity_1 <= rand_battery_1.capacity and capacity_2 <= rand_battery_2.capacity:
        return True
