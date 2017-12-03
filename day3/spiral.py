import sys
import math

def spiral(target):
    """
    Calculate Manhatten distance from a spiral starting at one
    to the target value 'target'.

    This did not turn out that pretty :-)
    """

    squares_covered = 1 # initially covering 1
    target_ring = 0
    while(squares_covered < target):
        target_ring += 1
        side_length = target_ring*2+1
        squares_covered += side_length*4-4 # don't count corners twice

    # calculate moves from center of target ring to the target
    last_side_length = target_ring*2+1
    last_ring_size = last_side_length*4-4
    last_ring_start = squares_covered - last_ring_size + 1

    # find the side on which the target is placed
    # giving each side a single corner
    lower = last_ring_start
    step = last_side_length-1
    while(target+1 > lower+step): lower+=step

    upper = lower+step
    middle = int(lower-1+(upper-lower)/2)
    steps_from_middle = abs(target - middle)

    return target_ring+steps_from_middle

print (spiral(int(sys.argv[1])))
