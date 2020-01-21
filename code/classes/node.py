from .algorithms import helpers
from .branch import Branch

class Node:
    def __init__(self, object):
        self.x = object.x
        self.y = object.y
        self.branch = None

    def get_distances(self, node):
        distances = []
        for branch in grid.branches:
            for node in branch:
                distances.append(helpers.distance(node, house))

    def get_closest_neighbour(self, node):
        closest = min(node.get_distances(node))
        return closest
