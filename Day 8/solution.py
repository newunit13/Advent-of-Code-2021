
with open('Day 8/input.txt', 'r') as f:
    data = f.readlines()

encoded_digits = []
problem_digits = []
for line in [line.split(' | ') for line in data]:
    encoded_digits.append(line[0])
    problem_digits.append(line[1].strip())


total_count = 0
for line_no, line in enumerate(problem_digits):
    words = line.split(' ')
    unique_counts = sum([1 for word in words if len(word) in [2, 3, 4, 7]])
    total_count += unique_counts

print('---')
print(f'Part 1: {total_count}')

def create_map(encoded_digits: str) -> dict:
    num_hash = {}
    segment_map = {}
    decoding_map = {}

    for digit in encoded_digits.split(' '):
        if len(digit) not in num_hash:
            num_hash[len(digit)] = [digit]
        else:
            num_hash[len(digit)].append(digit)

    chars = [char for char in encoded_digits if char != ' ']
    char_counts = Counter(chars)
    char_counts_flip = {}
    for char, count in char_counts.items():
        if count in char_counts_flip:
            char_counts_flip[count].add(char)
        else:
            char_counts_flip[count] = {char}

    segment_map['a'] = set(num_hash[3][0]) - set(num_hash[2][0])
    segment_map['b'] = char_counts_flip[6]
    segment_map['c'] = char_counts_flip[8] - segment_map['a']
    segment_map['e'] = char_counts_flip[4]
    segment_map['f'] = char_counts_flip[9]
    segment_map['g'] = char_counts_flip[7] - set(num_hash[4][0])
    segment_map['d'] = char_counts_flip[7] - segment_map['g']

    encoded_0 = frozenset(segment_map['a'] ^ segment_map['b'] ^ segment_map['c'] ^ segment_map['e'] ^ segment_map['f'] ^ segment_map['g'])
    encoded_1 = frozenset(segment_map['c'] ^ segment_map['f'])
    encoded_2 = frozenset(segment_map['a'] ^ segment_map['c'] ^ segment_map['d'] ^ segment_map['e'] ^ segment_map['g'])
    encoded_3 = frozenset(segment_map['a'] ^ segment_map['c'] ^ segment_map['d'] ^ segment_map['f'] ^ segment_map['g'])
    encoded_4 = frozenset(segment_map['b'] ^ segment_map['c'] ^ segment_map['d'] ^ segment_map['f'])
    encoded_5 = frozenset(segment_map['a'] ^ segment_map['b'] ^ segment_map['d'] ^ segment_map['f'] ^ segment_map['g'])
    encoded_6 = frozenset(segment_map['a'] ^ segment_map['b'] ^ segment_map['d'] ^ segment_map['e'] ^ segment_map['f'] ^ segment_map['g'])
    encoded_7 = frozenset(segment_map['a'] ^ segment_map['c'] ^ segment_map['f'])
    encoded_8 = frozenset('abcdefg')
    encoded_9 = frozenset(segment_map['a'] ^ segment_map['b'] ^ segment_map['c'] ^ segment_map['d'] ^ segment_map['f'] ^ segment_map['g'])

    decoding_map[encoded_0] = '0'
    decoding_map[encoded_1] = '1'
    decoding_map[encoded_2] = '2'
    decoding_map[encoded_3] = '3'
    decoding_map[encoded_4] = '4'
    decoding_map[encoded_5] = '5'
    decoding_map[encoded_6] = '6'
    decoding_map[encoded_7] = '7'
    decoding_map[encoded_8] = '8'
    decoding_map[encoded_9] = '9'
    

    return decoding_map

def decode(encoded_str: str, decoding_map: dict) -> str:
    return ''.join([decoding_map[frozenset(digit)] for digit in encoded_str.split()])

from collections import Counter

pn = 0
total = 0
for key, problem in zip(encoded_digits, problem_digits):

    map = create_map(key)
    decoded_problem = decode(problem, map)
    total += int(decoded_problem)

print(f'Part 2: {total}')
