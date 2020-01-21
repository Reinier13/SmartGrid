from ast import literal_eval as make_tuple

class Branch:
    def __init__(self):
        self.nodes = []

    def load_path(self):
        pass

    def add_nodes(self, object):
        node.get_closest_neighbour(node)

    def add_nodes(self, node, target):
        if node.x <= target.x:
            delta_x = list(range(node.x, target.x + 1))
        if node.x > target.x:
            delta_x = list(range(node.x, target.x - 1, -1))
        if node.y <= target.y:
            delta_y = list(range(node.y, target.y + 1))
        if node.y > target.y:
            delta_y = list(range(node.y, target.y - 1, -1))

        for x in delta_x:
            self.nodes.append('(%i,%i)' % (x,node.y))
        for y in delta_y:
            self.nodes.append('(%i,%i)' % (target.x,y))

        self.nodes = [make_tuple(cable.strip()) for node in self.nodes]
        self.nodes = list(dict.fromkeys(self.nodes))
