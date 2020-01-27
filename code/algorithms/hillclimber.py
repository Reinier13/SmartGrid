import random
import copy

class HillClimber:
    """
    The HillClimber class swaps random house(s) in a battery with another battery. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.cost = grid.calculate_cost()

    def multiple_swap(self, grid, opt):
        """
        Swap multiple houses at once
        """
        swap_battery_1 = choose_battery(grid)
        swap_houses_1 = []
        for i in range(opt):
            swap_house_1 = random.choice(swap_battery_1.houses)
            while swap_house_1 in swap_houses_1:
                swap_house_1 = random.choice(swap_battery_1.houses)
            swap_houses_1.append(swap_house_1)

        swap_battery_2 = choose_battery(grid)
        while swap_battery_1 == swap_battery_2:
            swap_battery_2 = choose_battery(grid)

        swap_houses_2 = []
        for i in range(opt):
            swap_house_2 = random.choice(swap_battery_2.houses)
            while swap_house_2 in swap_houses_2:
                swap_house_2 = random.choice(swap_battery_2.houses)
            swap_houses_2.append(swap_house_2)



    def mutate_grid(self, swap_houses_1, swap_houses_2, swap_battery_1, swap_battery_2, opt):
        """
        Changes the battery-house configuration
        """
        for i in range(opt):
            house_1 = swap_houses_1[i]
            house_2 = swap_houses_2[i]

            swap_battery_1.houses.append(swap_battery_2.houses.pop(swap_battery_2.houses.index(house_2)))
            swap_battery_2.houses.append(swap_battery_1.houses.pop(swap_battery_1.houses.index(house_1)))


    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_cost = new_grid.calculate_cost()
        old_cost = self.cost

        # We are looking for grids that cost less
        if new_value <= old_value:
            self.grid = new_grid
            self.cost = new_cost

    def run(self, iterations, opt, verbose=False):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid, opt=opt)

            # Accept it if it is better
            self.check_solution(new_grid)
