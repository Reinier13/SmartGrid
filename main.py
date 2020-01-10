from code.classes import grid
from code.algorithms import random, greedy

if __name__ == '__main__':
    test_grid = grid.Grid('input/wijk1_huizen.csv', 'input/wijk1_batterijen.csv')

    # random.random_connection(test_grid)
    #
    # for battery in test_grid.batteries:
    #     print(battery.houses)
    #     break
    #     # print(battery.houses)
    #     # print(len(battery.houses))

    greedy.greedy(test_grid)

    for battery in test_grid.batteries:
        print(battery.houses)
        print(battery.capacity_used())
        print(len(battery.houses))
