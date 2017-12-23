import copy

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

def first(grid, iterations):
    x, y = 0, 0
    dx, dy = 0, 1
    count = 0
    for _ in range(iterations):
        if grid.get((x,y), False):
            dx, dy = dy, -dx # turn right
            grid[(x, y)] = False
        else:
            dx, dy = -dy, dx # turn left
            grid[(x, y)] = True
            count += 1

        x += dx
        y += dy

    return count

def second(grid, iterations):
    x, y = 0, 0
    dx, dy = 0, 1
    count = 0
    for _ in range(iterations):
        node = grid.get((x,y), CLEAN)
        if node == CLEAN:
            dx, dy = -dy, dx # turn left
            grid[(x,y)] = WEAKENED
        elif node == WEAKENED:
            grid[(x,y)] = INFECTED
            count += 1
        elif node == INFECTED:
            dx, dy = dy, -dx # turn right
            grid[(x,y)] = FLAGGED
        elif node == FLAGGED:
            dx, dy = -dx, -dy # reverse
            grid[(x,y)] = CLEAN

        x += dx
        y += dy

    return count


def readGrid(file):
    lines = file.readlines()
    grid = {}
    midX = len(lines[0].strip())//2
    midY = len(lines)//2
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                xPos = x - midX
                yPos = midY - y
                grid[(xPos, yPos)] = INFECTED

    return grid

with open('input.in') as f:
    grid = readGrid(f)
    print(first(copy.deepcopy(grid), 10_000))
    print(second(grid, 10_000_000))
