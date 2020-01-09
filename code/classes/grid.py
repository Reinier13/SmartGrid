from .house import House
from .battery import Battery
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Grid:
    def __init__(self, houses_file, batteries_file):
        self.houses = self.load_houses(houses_file)
        # self.batteries = self.load_batteries(batteries_file)
        self.plot()


    def load_houses(self, houses_file):
        with open(houses_file, 'r') as houses_file:
            reader = csv.DictReader(houses_file)
            houses = []
            for row in reader:
                houses.append(House(row['x'], row[' y'], row[' max output']))
        print(houses)
        houses_file.close()
        return houses
<<<<<<< HEAD
    #
=======

>>>>>>> c64532e308a74ba9050f00fc2c299961818ca13c
    # def load_batteries(self, batteries_file):
    #     with open(batteries_file, 'r') as in_file:
    #         batteries = csv.DictReader(in_file)
    #         battery_dict = {}
    #         for row in batteries:
    #             battery_dict[row['positie']] = Battery(row['positie'], row[' capaciteit'])
    #
    #         print(battery_dict)
    #
    #     return battery_dict

    def plot(self):
        fig, ax = plt.subplots()
        for house in self.houses:
            ax.plot(house.x, house.y, 'ro')

        ax.set(xlabel='X-axis', ylabel='Y-axis', title='Grid')
        plt.grid()
        plt.show()
