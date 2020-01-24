import argparse

def parseArgs():
    """parseArgs.
    Parses arguments given to main and returns them
    Forces input for district and method if no arguments are given and sets
    number of iterations for kmeans to 50 if nothing is specified.
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
                        help = "Specify the method of initially assigning houses to batteries (greedy, random)",
                        choices = ["greedy","random"])
    parser.add_argument("-hc","--hillclimb",
                        help = "Specify which type of hill climb",
                        choices = ["single_swap", "multiple_swap", "simanneal"])
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
        args.part = "4"

    if args.method == None:
        args.method = input("Choose method: ")
        while args.method not in ["greedy","random"]:
            args.method = input("Choose method(\"greedy\" or \"random\"): ")


    return args