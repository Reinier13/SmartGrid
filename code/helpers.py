def distance(house, battery):
    """
    Calculates the distance between a house and a battery.
    """
    delta_x = house.x - battery.x
    delta_y = house.y - battery.y
    delta = abs(delta_x) + abs(delta_y)
    return delta 
