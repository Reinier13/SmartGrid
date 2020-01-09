class Battery:
    def __init__(self, positie, capacity):
        self.x = int(positie.split(', ')[0])
        self.y = int(positie.split(', ')[-1])
        self.capacity = float(capacity.strip(' '))
        # self.houses = {}

    # def add_house(self, house):
    #     self.houses[house.id] = house

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.capacity}]"
