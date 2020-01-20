class Graph:
    def __init__(self, grid):
        self.nodes = grid.houses
        self.edges = []
        # self.print(self.nodes)

    def print(self, nodes):
        for node in nodes:
            print(node)

    def add_edges(self):
        for house in self.houses:
