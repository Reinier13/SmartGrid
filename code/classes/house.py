from ast import literal_eval as make_tuple

class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
        self.connected = False
        # self.cables = [(30, 40), (31,40), (32,40), (32,41)]
        self.battery = None
        self.cables = []

    def add_cable(self):
        delta_x = list(range(self.x, self.battery.x))
        delta_y = list(range(self.y, self.battery.y))

        for x in delta_x:
            self.cables.append('(%i,%i)' % (x,self.y))
        for y in delta_y:
            self.cables.append('(%i,%i)' % (self.battery.x,y))

        self.cables = [make_tuple(cable.strip()) for cable in self.cables]

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
