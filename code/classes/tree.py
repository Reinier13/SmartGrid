from .node import Node

class Tree:
    """
    Class Tree has the nodes of a tree object as an attribute 
    and also contains a method to add notes to the tree.
    """
    def __init__(self):
        self.nodes = []

    def add_nodes(self, node, target):
        """
        Adds a branch filled with nodes to a tree object.
        """
        node_list = []
        if node.x <= target.x:
            delta_x = list(range(node.x, target.x + 1))
        if node.x > target.x:
            delta_x = list(range(node.x, target.x - 1, -1))
        if node.y <= target.y:
            delta_y = list(range(node.y, target.y + 1))
        if node.y > target.y:
            delta_y = list(range(node.y, target.y - 1, -1))

        for x in delta_x[:-1]:
            node_list.append(Node(x,node.y))
        for y in delta_y:
            node_list.append(Node(target.x,y))

        self.nodes.append(node_list)
        return node_list
