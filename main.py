class Grid(object):
    def __init__(self, x, y):
        self.x = [0:50]
        self.y = [0:50]
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
