from .classes import node, branch

def mst(grid):
    for battery in grid.batteries:
        branches = []
        initial = node.Node(battery)
        distances = []
        get_distances(initial)

        closest = node.get_closest_neighbour(initial)

        branches.append(node.add_branch(initial, closest))


        for branch in branches:
            for node in branch.nodes:
                node.get_closest_neighbour()
