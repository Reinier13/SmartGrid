class Battery:
    def __init__(self, positie, capacity):
        self.x = int(positie.split(', ')[0])
        self.y = int(positie.split(', ')[-1])
        self.capacity = float(capacity.strip(' '))
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def capacity_used(self):
        used_capacity = 0
        for house in self.houses:
            used_capacity += house.output

        return float(used_capacity)

    # def is_valid(self):
    #     if self.capacity_used < self.capacity:
    #         return True
    #     return False

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.capacity}]"
