class House(object):
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))

    def add_cable(self):
        pass

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
