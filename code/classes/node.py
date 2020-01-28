from code.algorithms.helpers import distance
import numpy as np

class Node:
    """
    Class Node has a position and methods to get a distance
    and find closest node.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distances(self, nodes):
        """
        Returns distance between two nodes.
        """
        distances = []
        for branch in nodes:
            for target in branch:
                distances.append(distance(self, target))
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
        print(closest)
        return nodes[closest]

    def __repr__(self):
        """
        Returns a readable overview when house object is printed
        """
        return f"Node at ({self.x}, {self.y})"
