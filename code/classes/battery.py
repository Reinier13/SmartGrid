class Battery:
    def __init__(self, positie, capacity):
        self.x = int(positie.split(', ')[0])
        self.y = int(positie.split(', ')[-1])
        self.capacity = float(capacity.strip(' '))
        self.cost = 5000
        self.houses = []
        self.distances = []

    def add_house(self, house):
        self.houses.append(house)

    def capacity_used(self):
        """
        Calculates the capacity used.
        """
        used_capacity = 0.0
        for house in self.houses:
            used_capacity += house.output
        return used_capacity

    def check_cap(self):
        if self.capacity_used() <= self.capacity:
            return True

    def clear(self):
        self.houses = []
        self.distances = []

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.capacity}]"
