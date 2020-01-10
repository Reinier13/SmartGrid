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
        ax = plt.axes()

        for house in self.houses:
            ax.scatter(house.x, house.y, c='r', marker='o')

        for battery in self.batteries:
            ax.scatter(battery.x, battery.y, c='b', marker='*')

        ax.set(xlabel='X-axis', ylabel='Y-axis', title='Grid')
        ax.grid()
        plt.show()
