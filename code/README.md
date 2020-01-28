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
  - Adds a house to the houses that are connected to the battery
- capacity_used()
  - Calculates the capacity used
- check_cap()
  - Checks whether the capacity of the battery is exceeded
- clear()
  - Clears the houses connected to the battery


### grid.py
**Grid-object**
##### Attributes:
- batteries
- houses
- trees
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
- nodes: The branch of node points the tree consists of

##### Methods:
- add_nodes()
  - Adds a branch filled with nodes to a tree object


# Algorithms

### random.py

#### Components:
- rand()
  - Random algorithm fill each battery with houses randomly
    until the capacity of the battery is reached

#### Flow:
- First the algorithm randomly shuffles order of how the houses saved in the grid object
- Iterating over all batteries and all houses, the batteries get filled until the capacity of the battery is reached
- If this random assignment of houses doesn't connect all 150 houses, it repeats the process
- Draw the grid


### greedy.py

#### Components:
- greedy()
  - Greedy algorithm that chooses a random battery and connects with houses
    that are closest until the capacity of the battery is reached
- draft()
  - Draft - Greedy algorithm that connects the batteries in turn with the houses
    that are closest to that battery until the capacity of the battery is
    reached
- fit()
  - After a greedy or draft algorithm is runned,
    houses have to be rearranged until every battery capacity is met
- arrange()
  - The house with the longest distance to battery with the most capacity used,
    gets rearranged to the battery with the least capacity used
- check_houses_cap()
  - Check if all houses are compliant to the capacity constraint. Return False
    if this is not the case
- create_distances()
  - Creates distances for all batteries from the battery to all its houses
- pick()
  - Gets the index of closest house to a battery
- remove_house()
  - Marks house as connected to a battery by setting the distance to a max

#### Flow

##### Greedy

- It iterates over all batteries 
- Then as long the battery capacity is not exceeded, the closest house is added
- When all the houses are connected, some battery capacities have exceeded, so fit() is called

##### Draft

- While there are still houses availabe, it iterates over all batteries
- Every battery picks the closest house
- When all the houses are connected, some battery capacities have exceeded, so fit() is called

##### Arrange

- For every battery the capacity is saved in a list
- The battery with the highest and lowest used capacity is identified
- For the battery with the highest used capacity, the house with the longest distance is transferred to the battery with the lowest used capacity


### determine_bound.py

#### Components:

- determine_bound()
  - Determine bound is an algorithm that connects every house to it's closest 
    or furthest battery, without a capacity constraint for the battery
- find_battery()
  - Connect the furthest or closest battery, dependent on the global counter,
    to a house

#### Flow:

- It iterates over every house and finds the battery with the longest or shortest distance to the house, without taking into account the capacity constraint of the batteries

### hillclimb.py

#### Components:

- 





  