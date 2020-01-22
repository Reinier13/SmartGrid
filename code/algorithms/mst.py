from code.classes import node, tree

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
