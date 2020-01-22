from code.classes import node, tree

def mst(grid):
    for battery in grid.batteries:
        tree_obj = tree.Tree()
        nodes = []
        nodes.append(node.Node(battery))
        for house in battery.houses:
            point = node.Node(house)
            closest_node = point.get_closest_node(nodes)
            tree_obj.add_nodes(point, closest_node)
            nodes.append(point)
        grid.trees.append(tree_obj.nodes)
