from .house import House
import csv

class Grid:
    def __init__(self, houses_file, batteries_file):
        self.houses = self.load_houses(houses_file)

    def load_houses(self, houses_file):
        with open(houses_file, 'r') as houses_file:
            houses = csv.DictReader(houses_file)
            houses_list = []
            for row in houses:
                houses_list.append(House(row['x'], row[' y'], row[' max output']))

        return houses_list

    def load_batteries
