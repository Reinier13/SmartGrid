from ast import literal_eval as make_tuple

class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
        self.battery = None
        self.cables = []
        self.distances = []

    def add_cable(self):
        if self.x <= self.battery.x:
            delta_x = list(range(self.x, self.battery.x + 1))
        if self.x > self.battery.x:
            delta_x = list(range(self.x, self.battery.x - 1, -1))
        if self.y <= self.battery.y:
            delta_y = list(range(self.y, self.battery.y + 1))
        if self.y > self.battery.y:
            delta_y = list(range(self.y, self.battery.y - 1, -1))

        for x in delta_x:
            self.cables.append('(%i,%i)' % (x,self.y))
        for y in delta_y:
            self.cables.append('(%i,%i)' % (self.battery.x,y))

        self.cables = [make_tuple(cable.strip()) for cable in self.cables]


    def __hash__(self):
        return hash((self.name, self.location))

    def __eq__(self, other):
        return (self.name, self.location) == (other.name, other.location)

    def __repr__(self):
        return f"House at ({self.x}, {self.y})"
