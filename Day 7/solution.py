import numpy as np
from collections import defaultdict

with open('Day 7/test.txt') as f:
    data = f.read()

with open('Day 7/input.txt') as f:
    data = f.read()



crab_ships = [int(ship.strip()) for ship in data.split(',')]
crab_ships = np.array(crab_ships)

median = np.median(crab_ships)

print(f'Part 1: {sum([abs(ship_pos - median) for ship_pos in crab_ships])}')

def calculate_distance(ship_pos: int, target_pos: int) -> int:
    return abs(ship_pos - target_pos)

def calculate_fuel_needed(spaces_away: int) -> int:
    return spaces_away * (spaces_away + 1) // 2

ship_hash = defaultdict(int)

for target in range(min(crab_ships), max(crab_ships) + 1):
    for ship in crab_ships:
        distance = calculate_distance(ship, target)
        fuel_needed = calculate_fuel_needed(distance)
        ship_hash[target] += fuel_needed

print(f'Part 2: {min(ship_hash.values())}')