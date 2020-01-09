from .house import House
from .battery import Battery
import csv

class Grid:
    def __init__(self, houses_file, batteries_file):
        self.houses = self.load_houses(houses_file)
        self.batteries = self.load_batteries(batteries_file)

    def load_houses(self, houses_file):
        with open(houses_file, 'r') as houses_file:
            houses = csv.DictReader(houses_file)
            houses_list = []
            for row in houses:
                houses_list.append(House(row['x'], row[' y'], row[' max output']))

        return houses_list

    def load_batteries(self, batteries_file):
        with open(batteries_file, 'r') as in_file:
            batteries = csv.DictReader(in_file)
            battery_dict = {}
            for row in batteries:
                battery_dict[row['positie']] = Battery(row['positie'], row[' capaciteit'])

            print(battery_dict)

        return battery_dict
