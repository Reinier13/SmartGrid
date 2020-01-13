from code.classes import grid
from code.algorithms import random, greedy,algo

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    algo.greedy(test_grid)


    test_grid.plot()
