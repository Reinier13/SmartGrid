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
<<<<<<< HEAD
        # print(test_grid.calculate_cost())
        swap.hill_climb(test_grid)
        # multiple_swap.hill_climb(test_grid, 2)
        # mst.mst(test_grid)
=======

        simanneal.simanneal(test_grid)
        # swap.hill_climb(test_grid)
<<<<<<< HEAD
        # multiple_swap.hill_climb(test_grid)
        print(test_grid.calculate_cost())
        # mst.mst(test_grid)
        # costs.append(test_grid.calculate_cost())

=======
        multiple_swap.hill_climb(test_grid, 1)
        mst.mst(test_grid)
>>>>>>> 4aff3dd5cf92e42bf2f4ace353981ffa332ebe93
        print(test_grid.calculate_cost())
>>>>>>> 571a31f58c631e31a737a5345cf44f8190bea8b6

    # print(test_grid.trees)

<<<<<<< HEAD
=======
    # display lowest cost
>>>>>>> 571a31f58c631e31a737a5345cf44f8190bea8b6
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # test_grid.histogram(costs, iterations)
    test_grid.plot(test_grid)
