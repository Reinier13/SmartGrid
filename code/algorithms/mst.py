from code.classes import node, tree

def mst(grid):
    nodes = []
    initial = node.Node(grid.batteries[0])
    nodes.append(initial)
    for house in grid.batteries[0].houses:
        house_node = node.Node(house)
        nodes.append(house_node)

    trees = tree.Tree()
    for point in nodes:
        closest_node = point.get_closest_node(nodes)
        trees.add_nodes(point, closest_node)
    return trees.nodes
