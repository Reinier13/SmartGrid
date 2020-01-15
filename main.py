from code.classes import grid
from code.algorithms import random, greedy, algo, master, draft, swap
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    draft.draft(test_grid)

    print(test_grid.calculate_cost())

    swap.hill_climb(test_grid)

    # test_grid.plot()

    print(test_grid.calculate_cost())
