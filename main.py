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
    def __init__(self, position, capacity):
        self.postition = postition
        self.capacity = capacity
        self.houses = houses

class Houses:
    def __init__(self, position, cables):
        self.position = position
        self.cables = cables

def main():
    print(import_file('input/wijk1_huizen.csv'))
    x = list(range(0, 51))
    y = list(range(0, 51))
    grid = [x, y]

    for coord in grid:
            print coord
