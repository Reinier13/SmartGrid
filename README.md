# SmartGrid
M4st3r_h4ck3rz

## Program usage
To run this program flags can be used.

    usage: main.py [-h] [-d {1,2,3}] [-p] [-m {greedy,random}
                   [-pt {1,2,3,4}]

    optional arguments:
      -h, --help            show this help message and exit

      -d {1,2,3}, --district {1,2,3}
                            Specify the number of the district (1, 2, 3)

      -p, --plot            Flag if plots should be made

      -m {greedy,random}, --method {greedy,random}
                            Specify the method of initially assigning houses to
                            batteries (greedy, random)

      -hc {single_swap,multiple_swap}, --method {single_swap,multiple_swap}
                            Specify which type of hill climb

      -s {1,2,3,4}, --swaps {1,2,3,4},
                            In case of multiple swaps, specify the number of houses to swap
        
      -sa, --simanneal,
                            Flag if hillclimb should be perfomed with simulated annealing      

      -pt {1,2,3,4}, --part {1,2,3,4}
                            Specifies until which part of the assignment the case
                            should be solved


To run it on district 1 in part 1 completely with a greedy way of connecting them while producing a plot the user, and performing a hillclimb with single_swap afterwards, would have to run

    "main.py -d 1 -m greedy -hc single_swap -p -pt 1"

To run it on district 1 in part 2 completely with a greedy way of connecting them while producing a plot the user, and performing a hillclimb with multiple swaps with 3 houses afterwards, would have to run

    "main.py -d 1 -m greedy -hc multiple_swap -s 3 -p -pt 2"