import sys

lookaround = [(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]
def calc_square(spiral, x, y):
    sum_of_neighbours = 0
    for (k,v) in lookaround:
        sum_of_neighbours += spiral.get((x-k,y-v), 0)

    return sum_of_neighbours

def stress_test(target):
    """
    Second half of day 3 of adventofcode 2017.

    Calculate the first value value larger than target
    in a regular spiral descension of integers where the values
    of each square is the sum of all its neighbors including diagonals.

    """
    spiral = {(0,0):1}
    y = dy = 0
    x = dx = 1
    while(True):
        val = calc_square(spiral, x, y)
        if (val > target): return val
        spiral[(x,y)] = val

        #https://stackoverflow.com/questions/398299/looping-in-a-spiral
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx

        x, y = x+dx, y+dy

print (stress_test(int(sys.argv[1])))
