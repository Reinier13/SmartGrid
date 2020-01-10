from .house import House
from .battery import Battery
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Grid:
    def __init__(self, houses_file, batteries_file):
        self.houses = self.load_houses(houses_file)
        self.batteries = self.load_batteries(batteries_file)
        self.plot()


    def load_houses(self, houses_file):
        with open(houses_file, 'r') as houses_file:
            reader = csv.DictReader(houses_file)
            houses = []
            for row in reader:
                houses.append(House(row['x'], row[' y'], row[' max output']))
        return houses

    def load_batteries(self, batteries_file):
        with open(batteries_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            batteries = []
            for row in reader:
                batteries.append(Battery(row['positie'].strip('[]'), row[' capaciteit']))
        return batteries

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # Major ticks every 20, minor ticks every 5
        major_ticks = np.arange(0, 51, 10)
        minor_ticks = np.arange(0, 51, 1)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # And a corresponding grid
        ax.grid(which='both')

        # Or if you want different settings for the grids:
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

        for house in self.houses:
            ax.scatter(house.x, house.y, c='r', marker='o', zorder=2)

        for battery in self.batteries:
            ax.scatter(battery.x, battery.y, c='b', marker='*', zorder=2)

        ax.set(xlabel='X-axis', ylabel='Y-axis', title='Grid')
        plt.show()
