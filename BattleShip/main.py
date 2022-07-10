from player import Player 
from ship import Ship


ship = Ship(5, 'Carrier')

coor = ship.vertical_coordinate()
ship.vertical_position(coor)
print(ship.position)

