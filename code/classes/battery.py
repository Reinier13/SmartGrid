class Battery:
    """
    Class Battery holds all necessary information about a battery, such as capacity and position.
    """
    def __init__(self, position, capacity):
        self.x = int(position.split(', ')[0])
        self.y = int(position.split(', ')[-1])
        self.capacity = float(capacity.strip(' '))
        self.cost = 5000
        self.houses = []
        self.distances = []
        self.tree = None

    def add_house(self, house):
        """
        Adds a house to the houses that are connected.
        """
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
        """
        Checks whether the capacity of the battery is exceeded.
        """
        if self.capacity_used() <= self.capacity:
            return True

    def clear(self):
        """
        Clears all the houses and "distances to houses" associated to the battery
        """
        self.houses = []
        self.distances = []

    def __repr__(self):
        """
        Returns a readable overview when battery object is printed
        """
        return f"[{self.x}, {self.y}, {self.capacity}]"
