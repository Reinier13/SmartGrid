from .house import House
from .battery import Battery
import csv
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import itertools


class Grid:
    def __init__(self, houses_file, batteries_file):
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)
        self.trees = []
        self.cost = set()


    def load_batteries(self, batteries_file):
        with open(batteries_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            batteries = []
            for row in reader:
                batteries.append(Battery(row['positie'].strip('[]'), row[' capaciteit']))
        return batteries


    def load_houses(self, houses_file):
        with open(houses_file, 'r') as houses_file:
            reader = csv.DictReader(houses_file)
            houses = []
            for row in reader:
                houses.append(House(row['x'], row[' y'], row[' max output']))
        return houses


    # def calculate_cost(self):
    #     self.cost = 0
    #     for battery in self.batteries:
    #         self.cost += battery.cost
    #     for house in self.houses:
    #         self.cost += (len(house.cables) - 1) * 9
    #     return self.cost

    def calculate_cost(self):
        self.cost = 0
        for battery in self.batteries:
            self.cost += battery.cost
        for tree in self.trees:
            for branch in tree:
                # print(branch)
                self.cost += ((len(branch) - 1) * 9)
        return self.cost


    def plot(self, grid):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # major ticks every 10, minor ticks every 1
        major_ticks = np.arange(0, 51, 10)
        minor_ticks = np.arange(0, 51, 1)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # a corresponding grid
        ax.grid(which='both')

        # settings for the grids
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

        # plot houses
        for house in self.houses:
            ax.scatter(house.x, house.y, c='r', marker='o', zorder=2)

<<<<<<< HEAD
            # # plot cables
=======
            # cablex = []
            # cabley = []
>>>>>>> 2cd3511d77dd4dca48c7a76851404fcbfa275dd9
            # for cable in house.cables:
            #     cablex.append(cable[0])
            #     cabley.append(cable[1])
            # ax.plot(cablex, cabley, '-', color='green')

<<<<<<< HEAD

=======
>>>>>>> 2cd3511d77dd4dca48c7a76851404fcbfa275dd9
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

        # plot batteries
        for battery in self.batteries:
            ax.scatter(battery.x, battery.y, c='b', marker='*', zorder=2)

        # set labels and show plot
        ax.set(xlabel='X-axis', ylabel='Y-axis', title='Grid')
        plt.show()


    def histogram(self, x, iterations):
        plt.hist(x, bins=iterations, edgecolor='black', facecolor='blue')
        plt.show()
        #  range=(50000,70000),
