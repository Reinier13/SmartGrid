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
            tree_obj.add_nodes(house, battery)
        grid.trees.append(tree_obj.nodes)
