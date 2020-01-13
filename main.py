from code.classes import grid
from code.algorithms import random, greedy

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')
    greedy.greedy(test_grid)
    test_grid.plot()

    print(test_grid.calculate_cost())
