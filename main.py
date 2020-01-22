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
        multiple_swap.hill_climb(test_grid, 1)
        mst.mst(test_grid)
        print(test_grid.calculate_cost())

    # print(test_grid.trees)

    # display lowest cost
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # test_grid.histogram(costs, iterations)
<<<<<<< HEAD
    test_grid.plot(test_grid)
=======
    test_grid.plot()
>>>>>>> d6aae226cd1f4597d87901d640f27230d713f16f
