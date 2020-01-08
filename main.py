import csv

with open('input/wijk1_huizen.csv') as houses:
    csv_reader = csv.reader(houses, delimiter=',')
    for row in csv_reader:
        pass

class Grid:
    def __init__(self, x, y):
        self.x = list(range(0, 50))
        self.y = list(range(0, 50))
        self.grid = [self.x, self.y]

        def populate(self):
            for coord in self.grid:
                print coord

class Battery:
    def __init__(self, x, y, cap):
        self.x = x
        self.y = y
        self.cap = capacity
        self.price = price
