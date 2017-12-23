CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

def main(grid, iterations):
    x, y = 0, 0
    dx, dy = 0, 1
    count = 0
    for _ in range(iterations):
        node = grid.get((x,y), CLEAN)
        if grid.get((x,y), False):
            dx, dy = dy, -dx # turn right
        else:
            dx, dy = -dy, dx # turn left

        if not grid.get((x,y), False):
            grid[(x, y)] = True
            count += 1
        else: 
            grid[(x, y)] = False

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
    print(main(grid, 10_000))
