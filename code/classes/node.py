from code.algorithms import helpers
import numpy as np

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distances(self, nodes):
        """
        Returns distance between two nodes.
        """
        distances = []
        for target in nodes:
            distances.append(helpers.distance(self, target))
        return distances

    def get_closest_node(self, nodes):
        """
        Returns closest node.
        """
        distances = self.get_distances(nodes)
        array = np.array(distances)
        closest = distances.index(np.partition(array, 0)[0])
        if len(nodes) > 1:
            closest = distances.index(np.partition(array, 1)[1])
        return nodes[closest]

    def __repr__(self):
        return f"Node at ({self.x}, {self.y})"
