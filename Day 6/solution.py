from collections import Counter

def age_fish(fish: Counter) -> Counter:
    new_fish = fish['0']
    fish['0'] = fish['1']
    fish['1'] = fish['2']
    fish['2'] = fish['3']
    fish['3'] = fish['4']
    fish['4'] = fish['5']
    fish['5'] = fish['6']
    fish['6'] = fish['7'] + new_fish
    fish['7'] = fish['8']
    fish['8'] = new_fish

#with open('Day 6/test.txt', 'r') as f:
#    data = f.read()

with(open('Day 6/input.txt', 'r')) as f:
    data = f.read()

starting_fish = [datum.strip() for datum in data.split(',')]

fish = Counter(starting_fish)

for day in range(256):
    age_fish(fish)
    #print(f'Day {day+1}: {fish}')
print(sum(fish.values()))
