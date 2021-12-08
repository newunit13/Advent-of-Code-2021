
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
winning_order = []
for callout in seq:
    called_out_numbers.add(callout)

    for board_num, board in enumerate(boards):
        for row_col in board:
            row_col = set(row_col)
            if row_col.issubset(called_out_numbers):
                board = [num for row in board[:5] for num in row if num not in called_out_numbers]
                board_total = sum(map(int, board))
                final_score = board_total * int(callout)

                print(f'''
Board #:        {board_num}
Board Total:    {board_total}
Final Callout:  {callout}
Final Score:    {final_score} ''')

                import sys
                sys.exit()
