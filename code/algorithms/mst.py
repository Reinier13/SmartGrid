import random
from code.classes import node, tree
from code.classes.grid import Grid

def mst(grid):
    grid.trees = []
    for battery in grid.batteries:
        battery.tree = tree.Tree()
        nodes = []
        nodes.append(node.Node(battery.x, battery.y))
        for house in battery.houses:
            house.node = node.Node(house.x, house.y)
            closest_node = house.node.get_closest_node(nodes)
            house.nodes = battery.tree.add_nodes(house.node, closest_node)
            for tree_list in battery.tree.nodes:
                for node_obj in tree_list:
                    nodes.append(node_obj)
        optimize(battery, nodes, battery.tree)
        grid.trees.append(battery.tree.nodes)


def optimize(battery, nodes, tree_obj):
    for i in range(300):
        house = random.choice(battery.houses)
        for node in house.nodes:
            nodes.remove(node)
        house.nodes = []
        closest_node = house.node.get_closest_node(nodes)
        house.nodes = tree_obj.add_nodes(house.node, closest_node)
        for tree_list in tree_obj.nodes:
            for node_obj in tree_list:
                nodes.append(node_obj)

def swap(grid):
    pass
