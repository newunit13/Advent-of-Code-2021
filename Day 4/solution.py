
# Get data
with open('Day 4/input.txt', 'r') as f:
    data = f.read()

# test data
#with open('Day 4/test.txt', 'r') as f:
#    data = f.read()

data = data.split('\n\n')
seq = data[0].split(',')
boards = data[1:]

# split boards into arrays
boards = [board.split('\n') for board in boards]
boards = [[row.split() for row in board if row] for board in boards]

# add columns to boards
for board in boards:
    for column in zip(*board):
        board.append(column)

called_out_numbers = set()
winning_order = dict()
for callout in seq:
    called_out_numbers.add(callout)

    for board_num, board in enumerate(boards):
        for row_col in board:
            row_col = set(row_col)
            if row_col.issubset(called_out_numbers):
                board = [num for row in board[:5] for num in row if num not in called_out_numbers]
                board_total = sum(map(int, board))
                final_score = board_total * int(callout)

                if board_num not in winning_order:
                    winning_order[board_num] = (board_num, board_total, final_score)

print("Part 1:", list(winning_order.values())[0])
print("Part 2:", list(winning_order.values())[-1])