import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, grid):
        self.battery = grid.batteries[0]
        self.houses = grid.houses
        self.edges = []
        # self.create_distances(grid, self.battery)
        # self.print(self.edges)
        self.add_edge(self.houses)

    def print(self, edges):
        print(edges)

    def distance(self, object1, object2):
        delta_x = object1.x - object2.x
        delta_y = object1.y - object2.y
        delta = abs(delta_x) + abs(delta_y)
        return delta

    # def create_distances(self, grid, battery):
    #     for object1 in grid.houses:
    #         list = []
    #         for object2 in grid.houses:
    #             list.append(self.distance(object1, object2))
    #         list.append(self.distance(object1, battery))
    #         self.edges.append(list)

    def add_edge(self, houses):
        G = nx.Graph()

        G.add_edge('a', 'b', weight=0.6)
        G.add_edge('a', 'c', weight=0.2)
        G.add_edge('c', 'd', weight=0.1)
        G.add_edge('c', 'e', weight=0.7)
        G.add_edge('c', 'f', weight=0.9)
        G.add_edge('a', 'd', weight=0.3)

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=6)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,
                               width=6, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        plt.axis('off')
        plt.show()
