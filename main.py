import csv

class House:
    def __init__(self, x, y, out):
        self.x = x
        self.y = y
        self.out = out

house_list = []

with open('wijk1_huizen.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)

    for x, y, output in reader:
        x = int(x)
        y = int(y)
        out = float(output)

        house_list.append(House(x, y, out))


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
