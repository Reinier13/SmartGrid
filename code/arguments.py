import argparse

def parseArgs():
    """
    Parses arguments given to main and returns them.
    Runs everything by default.
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
    parser.add_argument("-o","--optimize",
                        help = "Specify which type of optimization (single_swap, multiple_swap, simanneal)",
                        choices = ["single_swap", "multiple_swap", "simanneal"])
    parser.add_argument("-s","--swaps",
                        help = "In case of multiple swaps, specify the number of houses to swap(2 up to 14)",
                        choices = ["2","3","4","5","6","7","8","9","10","11","12","13","14"])
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

    if args.part in ["2","3","4"]:
        if args.optimize == None:
            args.optimize = input("Choose optimize option: ")
            while args.method not in ["single_swap", "multiple_swap", "simanneal"]:
                args.optimize = input("Choose optimize(\"single_swap\" or \"multiple_swap\" \"simanneal\"): ")

    if args.optimize == "multiple_swap":
        if args.swaps == None:
            args.swaps = input("Choose number of swaps: ")
            while args.swaps not in ["2","3","4","5","6","7","8","9","10","11","12","13","14"]:
                args.swaps = input("Choose number of swaps(2 up to 14): ")

    return args
