from .house import House
from .battery import Battery
from .tree import Tree
import csv
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import itertools
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


class Grid:
    """
    Class Grid holds other objects and has methods to load data 
    and make/clear connections.
    """
    def __init__(self, houses_file, batteries_file):
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)
        self.trees = []
        self.cost = set()


    def load_batteries(self, batteries_file):
        """
        Load all the batteries into the grid.
        """
        with open(batteries_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            batteries = []
            for row in reader:
                batteries.append(Battery(row['positie'].strip('[]'), row[' capaciteit']))
        return batteries


    def load_houses(self, houses_file):
        """
        Load all the houses into the grid.
        """
        with open(houses_file, 'r') as houses_file:
            reader = csv.DictReader(houses_file)
            houses = []
            for row in reader:
                houses.append(House(row['x'], row[' y'], row[' max output']))
        return houses


    def calculate_cost(self):
        """
        Calculate the costs of the whole grid system.
        """
        self.cost = 0
        for battery in self.batteries:
            self.cost += battery.cost
        for tree in self.trees:
            for branch in tree:
                self.cost += ((len(branch) - 1) * 9)
        return self.cost


    def draw(self):
        """
        Fill grid with trees of batteries and their corresponding houses.
        """
        self.trees = []
        for battery in self.batteries:
            tree_obj = Tree()
            for house in battery.houses:
                added_nodes = tree_obj.add_nodes(house, battery)
                house.nodes = added_nodes
            self.trees.append(tree_obj.nodes)


    def clear(self):
        """
        Clear all connections between batteries and houses.
        """
        for battery in self.batteries:
            for house in battery.houses:
                house.clear()
            battery.clear()


    def plot(self, grid, title):
        """
        Plot the grid system.
        """
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        major_ticks = np.arange(0, 51, 10)
        minor_ticks = np.arange(0, 51, 1)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

        for house in self.houses:
            ax.scatter(house.x, house.y, c='r', marker='o', zorder=2)

        colors = itertools.cycle(["r", "b", "g", "y", "k"])
        for tree in self.trees:
            c = next(colors)
            for branch in tree:
                cablex = []
                cabley = []
                for cable in branch:
                    cablex.append(cable.x)
                    cabley.append(cable.y)
                    ax.plot(cablex, cabley, '-', c=c)

        for battery in self.batteries:
            ax.scatter(battery.x, battery.y, c='b', marker='*', zorder=2)

        costs = grid.cost
        ax.set(xlabel='X-axis', ylabel='Y-axis', title=title + ", cost: " + str(costs))
        plt.show()


    def histogram(self, x, iterations):
        plt.hist(x, bins=iterations, edgecolor='black', facecolor='blue')
        plt.show()

    def simanneal_plot(self, coord_list):
        x = []
        y = []
        z = []
        for coord in coord_list:
            x.append(coord[0])
            y.append(coord[1])
            # z.append(coord[2])
        print(x[1],y[1])

        fig = plt.figure()
        # ax = fig.gca(projection='3d')

        # x = np.reshape(x, (10, 10, 10))
        # y = np.reshape(y, (10, 10, 10))
        # z = np.reshape(z, (10, 10, 10))

        x.reverse()
        x = np.asarray(x)
        y = np.asarray(y)
        X, Y = np.meshgrid(x, y)
        # z = np.asarray(x+y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)

        # fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(X, Y, Z)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()

        # fig = plt.figure()
        # ax = fig.gca(projection='3d')
        #
        # # Make data.
        # X = np.array(x)
        # Y = np.array(y)
        # # X, Y = np.meshgrid(X, Y)
        # Z = np.array(z)
        #
        # # Plot the surface.
        # surf = ax.plot_trisurf(X, Y, Z, cmap=cm.coolwarm,
        #                        linewidth=0, antialiased=False)
        #
        # # Customize the z axis.
        # ax.set_zlim(-1.01, 1.01)
        # ax.zaxis.set_major_locator(LinearLocator(10))
        # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #
        # # Add a color bar which maps values to colors.
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        #
        # plt.show()
