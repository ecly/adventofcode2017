def rotate(pattern):
    return [''.join(r) for r in list(zip(*pattern[::-1]))]

def flip(pattern):
    return pattern[::-1]

# generate all variations of keys for rules
def readRules(file):
    rules = {}
    for line in file:
        k, v = line.strip().split(' => ')
        key = k.split('/')
        to = v.split('/')
        for _ in range(4):
            rules[''.join(flip(key))] = to
            key = rotate(key)
            rules[''.join(key)] = to

    return rules

def main(rules, iterations):
    pattern = ".#./..#/###".split('/')

    for _ in range(iterations):
        step = 2 if len(pattern) % 2 == 0 else 3

        rows = []
        # Failed miserably at writing this this itereration myself so ended up entirely stealing
        # the work of -orez from the scoreboard. Shame!
        # https://github.com/orez-/Advent-of-Code-2017/blob/master/day21/original.py
        for y in range(0, len(pattern), step):
            rows.extend([] for _ in range(step + 1))
            for x in range(0, len(pattern), skktep):
                key = ''.join(pattern[y+dy][x+dx] for dy in range(step) for dx in range(step))
                for i, row in enumerate(rules[key], -step - 1):
                    rows[i].extend(row)
        pattern = rows

    return ''.join([''.join(r) for r in pattern]).count('#')

with open("input.in") as f:
    rules = readRules(f)
    print(main(rules, 5))
    print(main(rules, 18))

