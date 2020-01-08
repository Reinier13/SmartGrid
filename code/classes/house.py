class House:
    def __init__(self, position, cables):
        self.position = position
        self.cables = cables

    def __repr__(self):
        return self.position
