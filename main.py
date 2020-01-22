from code.classes import grid
from code.algorithms import random, draft, swap, greedy, mst, multiple_swap
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # initialize
    costs = []
    iterations = 1

<<<<<<< HEAD
    # greedy.greedy(test_grid)
    # simanneal.simanneal(test_grid)
    # generate multiple grids and apply hillclimb algorithm
    for i in range(iterations):
        random.rand(test_grid)
        print(test_grid.calculate_cost())
        swap.hill_climb(test_grid)
        print(test_grid.calculate_cost())
        mst.mst(test_grid)
        print(test_grid.calculate_cost())
=======
    greedy.greedy(test_grid)
    # generate multiple grids and apply hillclimb algorithm
    for i in range(iterations):
        random.rand(test_grid)
        multiple_swap.hill_climb(test_grid, 2)
        costs.append(test_grid.calculate_cost())
>>>>>>> 1a049f3d4e0fc306ee213dc73b6d99e818192ec5

    # display lowest cost
    print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # plot
    # test_grid.histogram(costs, iterations)
    test_grid.plot(test_grid)
