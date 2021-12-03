from collections import Counter

# set up data
with open('Day 3/input.txt', 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]


# Part 1
transposed = zip(*data)
gamma_rate = ''
epsilon_rate = ''

for digits in transposed:

    counts = Counter(digits)
    if counts['0'] > counts['1']:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

answer = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(answer) # 693486


# Part 2

def get_rating(function: str, numbers: list, position: int=0):
    if len(numbers) == 1:
        return int(numbers[0], 2)
    
    transposed = list(zip(*numbers))
    digits = transposed[position]
    counts = Counter(digits)

    if function == 'oxygen':
        significant_bit = counts.most_common(1)[0][0] if counts['0'] != counts['1'] else '1'
    elif function == 'co2':
        significant_bit = counts.most_common()[-1][0] if counts['0'] != counts['1'] else '0'
    else:
        raise Exception('Invalid function')

    results = [number for number in numbers if number[position] == significant_bit]

    return get_rating(function, results, position + 1)

oxygen_generate_rating = get_rating('oxygen', data)
co2_scrubber_rating = get_rating('co2', data)
answer = oxygen_generate_rating * co2_scrubber_rating

print(answer) # 3379326