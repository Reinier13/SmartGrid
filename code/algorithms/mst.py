import random
from code.classes import node, tree
from code.classes.grid import Grid
from .helpers import calculate_cost2

def mst(grid):
    
    for battery in grid.batteries:
        tree_obj = tree.Tree()
        nodes = []
        nodes.append(node.Node(battery.x, battery.y))
        for house in battery.houses:
            point = node.Node(house.x, house.y)
            closest_node = point.get_closest_node(nodes)
            tree_obj.add_nodes(point, closest_node)
            for tree_list in tree_obj.nodes:
                for node_obj in tree_list:
                    nodes.append(node_obj)
        grid.trees.append(tree_obj.nodes)

        # for house in battery.houses:


    # lowest = grid.calculate_cost()
    #
    # best_grid = Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')
    # for iter, battery in enumerate(best_grid.batteries):
    #     tree_obj2 = tree.Tree()
    #     nodes2 = []
    #     nodes2.append(node.Node(battery.x, battery.y))
    #     for i in range(2):
    #         print(i)
    #         random.shuffle(nodes2)
    #         for node2 in best_grid.houses:
    #             point2 = node.Node(node2.x, node2.y)
    #             closest_node2 = point2.get_closest_node(nodes2)
    #             tree_obj2.add_nodes(point2, closest_node2)
    #     best_grid.trees.append(tree_obj2.nodes)
    #     if best_grid.calculate_cost() < lowest:
    #         print('LOWER!\n')
    #         lowest = best_grid.calculate_cost()
    #         best = tree_obj2.nodes
    #         grid.trees[iter] = best
