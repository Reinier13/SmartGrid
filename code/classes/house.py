class House(object):
    def __init__(self, x, y, output):
        self.x = x
        self.y = y.strip(' ')
        self.output = output.strip(' ')

    def add_cable(self):
        pass

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
