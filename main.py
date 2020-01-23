from code.classes import grid
from code.algorithms import random, draft, swap, greedy, mst, multiple_swap, simanneal
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # initialize
    costs = []
    iterations = 1

    # generate multiple grids and apply hillclimb algorithm
    for i in range(iterations):
        random.rand(test_grid)

        simanneal.simanneal(test_grid)
        # swap.hill_climb(test_grid)
<<<<<<< HEAD
        multiple_swap.hill_climb(test_grid, 2)
        print(test_grid.calculate_cost())
        costs.append(test_grid.calculate_cost())

    # display lowest cost
    print(costs)
=======
        # multiple_swap.hill_climb(test_grid)
        print(test_grid.calculate_cost())
        # mst.mst(test_grid)
        # costs.append(test_grid.calculate_cost())


        multiple_swap.hill_climb(test_grid, 1)
        mst.mst(test_grid)
        print(test_grid.calculate_cost())

    # print(test_grid.trees)

    # print(min(costs))
>>>>>>> 89685328fcc4677448353db70af70d525adaba0f
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # test_grid.histogram(costs, iterations)
    test_grid.plot(test_grid)
