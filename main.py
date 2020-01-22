from code.classes import grid
<<<<<<< HEAD
from code.algorithms import random, draft, swap, greedy, mst, multiple_swap
import numpy as np
=======
from code.algorithms import random, draft, swap, greedy, mst, simanneal
import numpy as np

>>>>>>> a4cd31d310b134b427e06ba944f6a675bf8e5758

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # initialize
    costs = []
    iterations = 1

    greedy.greedy(test_grid)
    simanneal.simanneal(test_grid)
    # generate multiple grids and apply hillclimb algorithm
<<<<<<< HEAD
    for i in range(iterations):
        random.rand(test_grid)
        multiple_swap.hill_climb(test_grid)
        costs.append(test_grid.calculate_cost())
=======
    # for i in range(iterations):
    #     greedy.greedy(test_grid)
    #     swap.hill_climb(test_grid)
    #     tree = mst.mst(test_grid)
    #     costs.append(test_grid.calculate_cost())
>>>>>>> a4cd31d310b134b427e06ba944f6a675bf8e5758

    # display lowest cost
    print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # plot
    # test_grid.histogram(costs, iterations)
    test_grid.plot(test_grid)
