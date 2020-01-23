from code.classes import grid
from code.algorithms import random, draft, swap, greedy, mst, multiple_swap
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # initialize
    costs = []
    iterations = 1
    
    # generate multiple grids and apply hillclimb algorithm
    for i in range(iterations):
        random.rand(test_grid)
        # swap.hill_climb(test_grid)
        multiple_swap.hill_climb(test_grid, 2)
        print(test_grid.calculate_cost())
        costs.append(test_grid.calculate_cost())

    # display lowest cost
    print(costs)
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # plot
    # test_grid.histogram(costs, iterations)
    # test_grid.plot(test_grid)
