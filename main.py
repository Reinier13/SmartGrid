from code.classes import grid
from code.algorithms import random, greedy, hillclimb, simanneal, mst, determine_bound
from code.arguments import parseArgs
import numpy as np

def main():
    """
    Smart Grid by m4st3r_h4ck3rz_4_l1f3.mp3.
    Please refer to the README for more information.
    """
    # get arguments
    args = parseArgs()

    # specify paths for data to load
    housePath = "data/wijk" + args.district + "_huizen.csv"
    batteryPath = "data/wijk" + args.district + "_batterijen.csv"

    # load in data
    connect_grid = grid.Grid(housePath, batteryPath)

    # check which part of the assignment is requested
    if args.part == "1":
        first(args, connect_grid)
    if args.part == "2":
        second(args, connect_grid)
    if args.part == "3":
        third(args, connect_grid)
    if args.part == "4":
        fourth(args, connect_grid)

    return connect_grid

def first(args, grid):
    """
    Solves the first mission.
    """
    connect_grid = grid

    if args.method == "greedy":
        # connect all batteries with their nearest houses
        # one battery at a time
        greedy.greedy(connect_grid)
        print("Greedy costs:", connect_grid.calculate_cost())

    if args.method == "draft":
        # connect all batteries with their nearest houses
        # each battery taking turns picking a house
        greedy.draft(connect_grid)
        print("Draft costs:", connect_grid.calculate_cost())

    if args.method == "random":
        # connect all houses to random battery
        random.rand(connect_grid)
        print("Random costs:", connect_grid.calculate_cost())

    if args.plot:
        pass
        # connect_grid.plot(connect_grid, 'Initial')

    return connect_grid

def second(args, grid):
    """
    Solves the second mission.
    """
    connect_grid = first(args, grid)

    # check which type of hillclimb to run
    if args.optimize == "single_swap":
        hillclimb.hill_climb(connect_grid, 1)

    if args.optimize == "multiple_swap":
        # save the number of houses to swap simultanously
        opt = int(args.swaps)
        hillclimb.hill_climb(connect_grid, opt)

    if args.optimize == "simanneal":
        # simulated anneal
        coord_list = simanneal.simanneal(connect_grid)
    # update the cost
    print("Improved costs:", connect_grid.calculate_cost())

    if args.plot:
        pass
        # connect_grid.plot(connect_grid, 'After hill climb')
        # connect_grid.simanneal_plot(coord_list)

    return connect_grid

def third(args, grid):
    """
    Solve the third mission.
    """
    connect_grid = second(args, grid)

    # find a non-optimized minimal spanning tree
    mst.mst(connect_grid)

    print("MST costs:", connect_grid.calculate_cost())

    if args.plot:
        connect_grid.plot(connect_grid, "Shared cables")

    return connect_grid

def fourth(args, grid):
    """
    Solve the fourth mission.
    """
    connect_grid = third(args, grid)

    # find a optimized minimal spanning tree
    mst.mst(connect_grid)

    print("MST optimized costs:", connect_grid.calculate_cost())

    if args.plot:
        connect_grid.plot(connect_grid, "Shared cables optimized")

    return connect_grid

if __name__ == '__main__':
    main()
