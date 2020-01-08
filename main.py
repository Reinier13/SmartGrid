import csv

with open('input/wijk1_huizen.csv') as houses:
    csv_reader = csv.reader(houses, delimiter=',')
    for row in csv_reader:
        pass

class Battery:
    def __init__(self, x, y, cap):
        self.x = x
        self.y = y
        self.cap = capacity
        self.price = price

def main():
    x = list(range(0, 50))
    y = list(range(0, 50))
    grid = [x, y]

    for coord in grid:
            print coord
