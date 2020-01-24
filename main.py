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
<<<<<<< HEAD
        draft.draft(test_grid)
        # print(test_grid.calculate_cost())
        swap.hill_climb(test_grid)
        # multiple_swap.hill_climb(test_grid, 2)
        mst.mst(test_grid)
        print(test_grid.calculate_cost())

    # print(test_grid.trees)

    # display lowest cost
=======
        random.rand(test_grid)

        simanneal.simanneal(test_grid)
        # swap.hill_climb(test_grid)

        mst.mst(test_grid)

        #
        # multiple_swap.hill_climb(test_grid)
        print(test_grid.trees)
        print(test_grid.calculate_cost())


        # costs.append(test_grid.calculate_cost())


        # multiple_swap.hill_climb(test_grid, 1)
        # mst.mst(test_grid)
        # print(test_grid.calculate_cost())

    # print(test_grid.trees)

>>>>>>> 91c497a22086983729932bb91f0f313f678381d8
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # test_grid.histogram(costs, iterations)
    test_grid.plot(test_grid)
