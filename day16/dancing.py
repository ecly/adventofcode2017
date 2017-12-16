import itertools

def dance(moves, positions):
    l = list(positions)
    for m in moves:
        if m[0] == 's':
            val = int(m[1:])
            l = l[-val:]+l[:-val]
        elif m[0] == 'x':
            vals = m[1:].split('/')
            x, y = int(vals[0]), int(vals[1])
            l[x], l[y] = l[y], l[x]
        elif m[0] == 'p':
            x = l.index(m[1])
            y = l.index(m[3])
            l[x], l[y] = l[y], l[x]
    return ''.join(l)

with open('input.in') as f:
    moves = f.read().split(',')
    initial = 'abcdefghijklmnop'
    print(dance(moves, initial))
    seen = [initial]
    current = initial
    for i in itertools.count(1): # count from one
        current = dance(moves, current)
        if current == initial: # we've gone full circle
            print(seen[1_000_000_000 % i])
            break
        else: 
            seen.append(current)
