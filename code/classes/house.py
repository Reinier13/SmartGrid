class House:
    """
    Class House holds all necessary information about a house, such as output and position.
    """
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
        # construct all grid points between a battery and house
        if self.x <= self.battery.x:
            delta_x = list(range(self.x, self.battery.x + 1))
        if self.x > self.battery.x:
            delta_x = list(range(self.x, self.battery.x - 1, -1))
        if self.y <= self.battery.y:
            delta_y = list(range(self.y, self.battery.y + 1))
        if self.y > self.battery.y:
            delta_y = list(range(self.y, self.battery.y - 1, -1))

        # make node objects of all grid points
        node_list = []
        for x in delta_x[:-1]:
            node_list.append(Node(x, self.y))
        for y in delta_y:
            node_list.append(Node(self.battery.x, y))

        # append node objects to cables attribute
        self.cables.append(node_list)

    def clear(self):
        """
        Clears the battery associated to the house object 
        and clears cables to battery
        """
        self.battery = None
        self.cables = []


    def __repr__(self):
        """
        Returns a readable overview when house object is printed
        """
        return f"House at ({self.x}, {self.y}) with output: {self.output}"
