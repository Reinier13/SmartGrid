class House(object):
    def __init__(self, x, y, output):
<<<<<<< HEAD
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
=======
        self.x = x
<<<<<<< HEAD
        self.y = y
        self.output = float(output)
        self.cables = {}

=======
        self.y = y.strip(' ')
        self.output = output.strip(' ')
>>>>>>> 256edc2494065c0923685f9128700ee8c7e5ab40

    def add_cable(self):
        pass
>>>>>>> e1e2b4301f66039ef79b5b10621d17c3994a8a45

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
