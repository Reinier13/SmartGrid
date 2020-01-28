# Classes

### house.py
**House-object**
##### Attributes:
- x, y: Location
- output: Output of the house
- node: Node point of the house
- nodes: The branch of node points connected to the house
- battery: The battery it's connected to
- distances: The distances from the house to every battery

##### Methods:
- clear()
  - Clears the battery connected to the house object 


### battery.py
**Battery-object**
##### Attributes:
- x, y: Location
- capacity: Capacity of the battery
- cost: The cost of the battery
- houses: The houses connected to this battery
- distances: The distances from the battery to every house
- tree: The tree this battery makes with all the node points connected all the houses and the battery itself
- nodes: The branch of node points connected to the battery

##### Methods:
- add_house()
  - Adds a house to the houses that are connected to the battery.
- capacity_used()
  - Calculates the capacity used.
- check_cap()
  - Checks whether the capacity of the battery is exceeded.
- clear()
 - Clears the houses connected to the battery


### grid.py
**Grid-object**
##### Attributes:
- batteries
- houses
- tree
- cost: cost of the whole configuration


##### Methods:
- load_batteries()
  - Load all the batteries into the grid
- load_houses()
  - Load all the houses into the grid
- calculate_cost()
  - Calculate the costs of the whole grid system
- draw()
  - Fill grid with trees of batteries and their corresponding houses
- clear()
  - Clear all connections between batteries and houses
- plot()
  - Plot the grid system
- histogram()
  - Plot a histogram of costs
- simanneal_plot()
  - Plot a heatmap of costs, with different temperatures and cooling rates


### node.py
**Node-object**
##### Attributes:
- x, y: Location

##### Methods:
- get_distances()
  - Returns distance between two nodes
- get_closest_node()
  - Returns closest node to the node object


### tree.py
**Tree-object**
##### Attributes:
- nodes: The branch of node point the tree consists of

##### Methods:
- add_branch()
  - Adds a branch filled with nodes to a tree object


# Algorithms
