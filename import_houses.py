from main import House
import csv

def import_file(file):
    with open(file, newline='') as houses_file:
        houses = csv.reader(houses_file)
        next(houses, None)
        houses_list = []
        for x, y, output in houses:
            x = int(x)
            y = int(y)
            output = float(output)
            house_list.append(House(x, y, output))
    return house_list
