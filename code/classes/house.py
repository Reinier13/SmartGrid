class House(object):
    def __init__(self, x, y, output):
        self.x = x
<<<<<<< HEAD
        self.y = y
        self.output = float(output)
        self.cables = {}

=======
        self.y = y.strip(' ')
        self.output = output.strip(' ')

    def add_cable(self):
        pass
>>>>>>> e1e2b4301f66039ef79b5b10621d17c3994a8a45

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
