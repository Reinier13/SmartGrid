class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y.strip(' '))
        self.output = float(output.strip(' '))
        self.connected = False
<<<<<<< HEAD
        self.cables = []
=======
        self.cables = [(30, 40), (31,40), (32,40), (32,41)]
>>>>>>> e13fb4318f8887cbaa9880287c4b7887f3b2462e

    def add_cable(self):
        pass

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.output}]"
