class House:
    def __init__(self, x, y, output):
        self.x = x
        self.y = y
        self.output = float(output)

    def __repr__(self):
        return f"({self.x}, {self.y}) - output:{self.output}"
