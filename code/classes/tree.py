from ast import literal_eval as make_tuple

class Tree:
    def __init__(self):
        self.nodes = []

    def add_nodes(self, node, target):
        node_list = []
        if node.x <= target.x:
            delta_x = list(range(node.x, target.x + 1))
        if node.x > target.x:
            delta_x = list(range(node.x, target.x - 1, -1))
        if node.y <= target.y:
            delta_y = list(range(node.y, target.y + 1))
        if node.y > target.y:
            delta_y = list(range(node.y, target.y - 1, -1))

        for x in delta_x:
            node_list.append((x,node.y))
        for y in delta_y:
            node_list.append((target.x,y))

        self.nodes.append(node_list)
