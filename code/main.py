from classes import grid
from algorithms import random

if __name__ == '__main__':
    test_grid = grid.Grid('../input/wijk1_huizen.csv', '../input/wijk1_batterijen.csv')

    # random.random_connection(test_grid)

    print(test_grid.batteries.houses)
