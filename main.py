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
        multiple_swap.hill_climb(test_grid)
        costs.append(test_grid.calculate_cost())

    # display lowest cost
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # plot
    test_grid.histogram(costs, iterations)
    test_grid.plot(tree)
