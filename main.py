from code.classes import grid
from code.algorithms import random, draft, swap, greedy
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # initialize
    costs = []
    iterations = 1

    # greedy.greedy(test_grid)
    #
    # print(test_grid.calculate_cost())

    # draft.draft(test_grid)
    #
    # print(test_grid.calculate_cost())

    # generate multiple grids and apply hillclimb algorithm
    for i in range(iterations):
        greedy.greedy(test_grid)
        swap.hill_climb(test_grid)
        costs.append(test_grid.calculate_cost())

    # display lowest cost
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))

    # plot
    # test_grid.histogram(costs, iterations)
    test_grid.plot()
