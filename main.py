from import_houses import import_file

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
