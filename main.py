<<<<<<< HEAD
<<<<<<< HEAD
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

=======
from import import import_file
>>>>>>> af15ee299d8d007d99ad2baae357c9b9116c5617
=======
from import_houses import import_file
>>>>>>> fcf6acb38c0d2ade615a8e2a20bd929195ca483a

class Battery:
    def __init__(self, position, capacity):
        self.postition = position
        self.capacity = capacity
        self.houses = houses

class Houses:
    def __init__(self, position, output, cables):
        self.position = position
        self.output = output
        self.cables = cables

def main():
    print(import_file('input/wijk1_huizen.csv'))
    x = list(range(0, 50))
    y = list(range(0, 50))
    grid = [x, y]

    for coord in grid:
        print(coord)

main()
