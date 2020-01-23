from ast import literal_eval as make_tuple
from .node import Node

class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
        self.battery = None
        self.cables = []
        self.distances = []


    def add_cable(self):
        node_list = []
        if self.x <= self.battery.x:
            delta_x = list(range(self.x, self.battery.x + 1))
        if self.x > self.battery.x:
            delta_x = list(range(self.x, self.battery.x - 1, -1))
        if self.y <= self.battery.y:
            delta_y = list(range(self.y, self.battery.y + 1))
        if self.y > self.battery.y:
            delta_y = list(range(self.y, self.battery.y - 1, -1))

        for x in delta_x[:-1]:
            node_list.append(Node(x, self.y))
        for y in delta_y:
            node_list.append(Node(self.battery.x, y))

        self.cables.append(node_list)


    def __repr__(self):
        return f"House at ({self.x}, {self.y})"
