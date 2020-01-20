from code.classes import grid, graph
from code.algorithms import random, draft, swap
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    graph.Graph(test_grid)

    # # initialize
    # costs = []
    # iterations = 100
    #
    # # generate multiple grids and apply hillclimb algorithm
    # for i in range(iterations):
    #     random.random(test_grid)
    #     swap.hill_climb(test_grid)
    #     costs.append(test_grid.calculate_cost())
    #
    # # display lowest cost
    # print(min(costs))
    # print(max(costs))
    # print(sum(costs)/len(costs))
    #
    # # plot
    # test_grid.histogram(costs, iterations)
    # test_grid.plot()
