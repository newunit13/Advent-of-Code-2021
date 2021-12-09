
#with open('Day 5/test.txt', 'r') as f:
#    data = f.readlines()

with open('Day 5/input.txt', 'r') as f:
    data = f.readlines()

class Line():
    def __init__(self, xy1 ,xy2):
        xy1 = xy1.split(',')
        xy2 = xy2.split(',')
        self.x1 = int(xy1[0])
        self.y1 = int(xy1[1])
        self.x2 = int(xy2[0])
        self.y2 = int(xy2[1])

    def __repr__(self):
        return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'

class Grid():
    def __init__(self, size_x, size_y):
        self.grid = [[0 for x in range(size_x)] for y in range(size_y)]

    def overlap(self):
        return [x for row in self.grid for x in row if x > 1]

    def add_line(self, line):
        x1,y1,x2,y2 = line.x1, line.y1, line.x2, line.y2
        for x in range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1):
            for y in range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1):
                self.grid[y][x] += 1

    def add_diag(self, line):
        x1,y1,x2,y2 = line.x1, line.y1, line.x2, line.y2
        for x, y in zip(range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1), range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1)):
            self.grid[y][x] += 1

    def __repr__(self):
        return '\n'.join([' '.join(list(map(str, row))) for row in self.grid])

    def __str__(self):
        return '\n'.join([' '.join(list(map(str, row))) for row in self.grid])

data = [datum.strip() for datum in data]
data = [datum.split(' -> ') for datum in data]
data = [Line(*datum) for datum in data]

grid = Grid(1000, 1000)

for line in data:
    if line.x1 == line.x2 or line.y1 == line.y2:
        grid.add_line(line)
    else:
        grid.add_diag(line)

print(len(grid.overlap()))