from code.classes import grid
from code.algorithms import random, greedy, algo, master, draft, swap
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')
    costs = []
    for i in range(30):
        greedy.greedy(test_grid)
        swap.hill_climb(test_grid)
        costs.append(test_grid.calculate_cost())
    test_grid.histogram(costs)
