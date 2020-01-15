from code.classes import grid
from code.algorithms import random, greedy, algo, master, draft
import numpy as np

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

<<<<<<< HEAD
    master.greedy(test_grid)
=======
    draft.draft(test_grid)
>>>>>>> 79964bd2da2dc16fce92d2b23a703d03365a65ad

    test_grid.plot()

    print(test_grid.calculate_cost())
