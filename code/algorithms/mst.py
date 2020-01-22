from code.classes import node, tree

def mst(grid):
    for battery in grid.batteries:
        trees = tree.Tree()
        nodes = []
        initial = node.Node(battery)
        nodes.append(initial)
        for house in battery.houses:
            point = node.Node(house)
            closest_node = point.get_closest_node(nodes)
            trees.add_nodes(point, closest_node)
            nodes.append(point)
        grid.trees.append(trees.nodes)
