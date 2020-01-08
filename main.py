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
