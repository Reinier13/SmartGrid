class Battery:
    def __init__(self, position, capacity):
        self.position = position
        self.capacity = capacity
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def __repr__(self):
        return self.position
