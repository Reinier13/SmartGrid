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
