import numpy as np

with open('Day 7/test.txt') as f:
    data = f.read()

with open('Day 7/input.txt') as f:
    data = f.read()



crab_ships = [int(ship.strip()) for ship in data.split(',')]
crab_ships = np.array(crab_ships)

median = np.median(crab_ships)

print(f'Part 1: {sum([abs(ship_pos - median) for ship_pos in crab_ships])}')

