class Grid(object):
    def __init__(self, x, y):
        self.x = [0:50]
        self.y = [0:50]
        self.grid = [self.x, self.y]

<<<<<<< HEAD
    def test(self):
        print('hallo')
        self.hallo = hallo

class Battery:
    def __init__(self, x, y, cap):
        self.x = x
        self.y = y 
        self.cap = capacity
        self.price = price
=======
    def populate(self):
        for coord in self.grid:
            print coord
>>>>>>> cf2ed24ad4547bd08b7e17a0b377a7b406d2e65c
