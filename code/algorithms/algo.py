import random, math

def greedy(grid):
    for house in grid.houses:
        for battery in grid.batteries:
            house.distances.append(distance(house, battery))
        print(house.distances)

        

def distance(house, battery):
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta
