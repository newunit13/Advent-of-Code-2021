
# Set up data
with open('Day 1/input.txt', 'r') as f:
    data = f.readlines()
    nums = [int(x) for x in data]

# Part One
answer = 0
for n1, n2 in zip(nums, nums[1:]):
    if n1 < n2:
        answer += 1

print(answer)


# Part Two
answer = 0
for i in range(len(nums)):
    win1 = sum(nums[i:i+3])
    win2 = sum(nums[i+1:i+4])

    if win1 < win2:
        answer += 1

print(answer)