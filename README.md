# SmartGrid

Electricity generation is being done by a lot of households nowadays. How to save this energy efficiently/economically is an complex problem. We will use heuristic methods to find our solutions. 
 
In this case There are 3 dummy neighborhoods, with each 150 houses and 5 batteries. Every house has it’s own output of energy. Every battery has it’s own capacity to store this energy. Houses are connected by cables. Each cable and battery is going to cost money. Goal of this project: connect these batteries and houses as cost-efficient as possible!

### The assignment was split into four parts:
1. Connecting all houses to a battery in all districts, the houses can't share a cable
2. Optimizing the connections in pt. 1
3. Connecting all houses to a battery in all districts, with the houses sharing their cables
4. Optimizing these connections in pt. 2


### Requirements

This code is written in Python 3.7. In requirements.txt all packages necessary for this project are stored. These can be installed with the following command.

```
pip install -r requirements.txt
```

## Program usage
To run this program flags can be used.

    usage: main.py [-h] [-d {1,2,3}] [-p] [-m {greedy,random}
                   [-pt {1,2,3,4}]

    optional arguments:
      -h, --help            show this help message and exit

      -d {1,2,3}, --district {1,2,3}
                            Specify the number of the district (1, 2, 3)

      -p, --plot            Flag if plots should be made

      -m {greedy, draft, random}, --method {greedy,random}
                            Specify the method of initially assigning houses to
                            batteries (greedy, random)

      -o {single_swap,multiple_swap, simanneal}, --method {single_swap,multiple_swap,simanneal}
                            Specify which type of optimization

      -s {2, up to, 14}, --swaps {2, up to, 14},
                            In case of multiple swaps, specify the number of houses to swap    

      -pt {1,2,3,4}, --part {1,2,3,4}
                            Specifies until which part of the assignment the case
                            should be solved


To run it on district 1 in part 2 completely with a greedy way of connecting them while producing a plot the user, and performing a hillclimb with single_swap afterwards, would have to run

    "main.py -d 1 -m greedy -o single_swap -p -pt 2"

To run it on district 1 in part 2 completely with a greedy way of connecting them while producing a plot the user, and performing a hillclimb with multiple swaps with 3 houses afterwards, would have to run

    "main.py -d 1 -m greedy -o multiple_swap -s 3 -p -pt 2"

### Structure

The following list describes the most important folders of this repository:

- **/code**: contains all code for this project
  - **/code/algorithms**: contains code for the algorithm
  - **/code/classes**: contains code for the classes
- **/data**: contains different csv files with the data of the neighborhoods stored

## Auteurs
- Reinier Boon
- Pieter Hoppenbrouwers
- Armin Mirrezai