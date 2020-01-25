import argparse

def parseArgs():
    """parseArgs.
    Parses arguments given to main and returns them
    Runs everything by default
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--district",
                        help = "Specify the number of the district (1, 2, 3)",
                        choices = ["1","2","3"])
    parser.add_argument("-p","--plot",
                        help = "Flag if plots should be made",
                        action = "store_true")
    parser.add_argument("-m","--method",
                        help = "Specify the method of initially assigning houses to batteries (greedy, random, draft)",
                        choices = ["greedy","random", "draft"])
    parser.add_argument("-hc","--hillclimb",
                        help = "Specify which type of hill climb",
                        choices = ["single_swap", "multiple_swap"])
    parser.add_argument("-s","--swaps",
                        help = "In case of multiple swaps, specify the number of houses to swap",
                        choices = ["1","2","3","4"])
    parser.add_argument("-sa","--simanneal",
                        help = "Flag if hillclimb should be perfomed with simulated annealing",
                        action = "store_true")
    parser.add_argument("-pt","--part",
                        help = "Specifies until which part of the assignment the case should be solved",
                        choices = ["1","2","3","4"])
    args = parser.parse_args()

    # Force valid input of required arguments
    if args.district == None:
        args.district = input("Choose district: ")
        while args.district not in ["1","2","3"]:
            args.district = input("Choose district(1, 2 or 3): ")

    if args.part == None:
        args.part = "1"

    if args.method == None:
        args.method = input("Choose method: ")
        while args.method not in ["greedy","random", "draft"]:
            args.method = input("Choose method(\"greedy\" or \"random\" \"draft\"): ")

    if args.part in ["2", "3", "4"]:
        if args.hillclimb == None:
            args.hillclimb = input("Choose hillclimb: ")
            while args.method not in ["single_swap", "multiple_swap"]:
                args.hillclimb = input("Choose hillclimb(\"single_swap\" or \"multiple_swap\"): ")

    if args.hillclimb == "multiple_swap":
        if args.swaps == None:
            args.swaps = input("Choose number of swaps: ")
            while args.swaps not in ["1","2","3", "4"]:
                args.swaps = input("Choose number of swaps(1, 2, 3 or 4): ")

    return args
