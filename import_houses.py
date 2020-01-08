import csv

def import_file(file):
    with open(file) as houses_file:
        houses = csv.reader(houses_file, delimiter=',')
        for x, y, capacity in houses:
            return x, y, capacity
