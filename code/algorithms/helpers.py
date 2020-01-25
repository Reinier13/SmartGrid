from code.classes import tree

def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta

def draw(grid):
    grid.trees = []
    for battery in grid.batteries:
        tree_obj = tree.Tree()
        for house in battery.houses:
            added_nodes = tree_obj.add_nodes(house, battery)
            house.nodes = added_nodes
        grid.trees.append(tree_obj.nodes)

def clear(grid):
    for battery in grid.batteries:
        battery.clear()
        for house in battery.houses:
            house.clear()
