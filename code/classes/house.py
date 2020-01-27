class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
        self.node = None
        self.nodes = []
        self.battery = None
        self.cables = []
        self.distances = []


    def add_cable(self):
        """
        Adds a branch filled with nodes to a house.
        """

        # retrieve all coordinates from battery to house
        node_list = []
        if self.x <= self.battery.x:
            delta_x = list(range(self.x, self.battery.x + 1))
        if self.x > self.battery.x:
            delta_x = list(range(self.x, self.battery.x - 1, -1))
        if self.y <= self.battery.y:
            delta_y = list(range(self.y, self.battery.y + 1))
        if self.y > self.battery.y:
            delta_y = list(range(self.y, self.battery.y - 1, -1))

        # make node objects of all coordinates
        for x in delta_x[:-1]:
            node_list.append(Node(x, self.y))
        for y in delta_y:
            node_list.append(Node(self.battery.x, y))

        self.cables.append(node_list)

    def clear(self):
        self.battery = None
        self.cables = []


    def __repr__(self):
        return f"House at ({self.x}, {self.y}) with output: {self.output}"
