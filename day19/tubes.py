def bounds(x,y,graph):
    return 0 <= y < len(graph) and 0 <= x < len(graph[y])

def collect_letters(graph):
    x, y = graph[0].index('|'), 0
    dx, dy = 0, 1
    letters = []
    while True:
        if bounds(x+dx, y+dy, graph) and graph[y+dy][x+dx] != ' ':
            x += dx
            y += dy
            if graph[y][x].isalpha():
                letters.append(graph[y][x])

        elif bounds(x+dy, y+dx, graph) and graph[y+dx][x+dy] != ' ':
            dx, dy = dy, dx
        elif bounds(x+dy, y-dx, graph) and graph[y-dx][x+dy] != ' ':
            dx, dy = dy, -dx
        elif bounds(x-dy, y+dx, graph) and graph[y+dx][x-dy] != ' ':
            dx, dy = -dy, dx
        else:
            return letters

with open('input.in') as f:
    graph = f.read().splitlines()
    print(collect_letters(graph))
