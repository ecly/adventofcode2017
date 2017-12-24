def bridges(pieces, bridge=[], port=0):
    matches = list(filter(lambda piece: port in piece, pieces))
    if matches == []:
        yield bridge

    for match in matches:
        remaining = pieces[:]
        remaining.remove(match)
        newPort = match[:]
        newPort.remove(port)
        yield from bridges(remaining, bridge+[match], newPort[0])

with open('input.in') as f:
    pieces = [list(map(int, line.split('/'))) for line in f.readlines()]
    stats = list(map(lambda bridge: (len(bridge), sum([sum(part) for part in bridge])), bridges(pieces)))
    print(max(stats, key=lambda stat: stat[1])[1])
    print(max(stats, key=lambda stat: stat[0])[1])
