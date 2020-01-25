from code.classes import grid
from code.algorithms import random, draft, swap, greedy, mst, multiple_swap, simanneal
from code.algorithms.arguments import parseArgs
import numpy as np

def main():
    """ Smart Grid by m4st3r_h4ck3rs
        Please refer to the README for more information.
    """

    # Get arguments
    args = parseArgs()
    # Specify paths for data to load
    housePath = "input/wijk" + args.district + "_huizen.csv"
    batteryPath = "input/wijk" + args.district + "_batterijen.csv"

    # Load in data
    connect_grid = grid.Grid(housePath, batteryPath)

    if args.part == "1":
        if args.method == "greedy":
            # Connect all houses to nearest battery
            greedy.greedy(connect_grid)
            print("Initial costs: ", connect_grid.calculate_cost())

        if args.method == "random":
            # Connect all houses to random battery
            random.rand(connect_grid)
            print("Initial costs: ", connect_grid.calculate_cost())

        if args.plot:
           connect_grid.plot(connect_grid, 'Initial')

    if args.part == "2":
        if args.method == "greedy":
            # Connect all houses to nearest battery
            greedy.greedy(connect_grid)
            print("Initial costs: ", connect_grid.calculate_cost())

        if args.method == "random":
            # Connect all houses to random battery
            random.rand(connect_grid)
            print("Initial costs: ", connect_grid.calculate_cost())

        if args.plot:
           connect_grid.plot(connect_grid, 'Initial')

        if args.hillclimb == "single_swap":
            swap.hill_climb(connect_grid)
        if args.hillclimb == "multiple_swap":
            opt = int(args.swaps)
            multiple_swap.hill_climb(connect_grid, opt)

        if args.plot:
           connect_grid.plot(connect_grid, 'After hill climb')

    if args.part == "3":
        # Connect all houses to nearest battery
        mst.mst(connect_grid)
        print("Initial costs: ", connect_grid.calculate_cost())

        if args.plot:
           connect_grid.plot(connect_grid, "Initial")

    if args.part == "4":
        pass

    print("Final cost: ", connect_grid.cost)

    if args.plot:
        connect_grid.plot(connect_grid, "Final")

    return connect_grid


if __name__ == '__main__':
    main()
