import copy
import collections
import re

def parse(file):
    reg = 'p=<(.*)>, v=<(.*)>, a=<(.*)>'
    particles = []
    for line in file:
        res = re.search(reg, line)
        p = list(map(int, res.group(1).split(',')))
        v = list(map(int, res.group(2).split(',')))
        a = list(map(int, res.group(3).split(',')))
        particles.append([p,v,a])
    return particles
    
def step(particle):
    particle[1] = [x + dx for x, dx in zip(particle[1], particle[2])]
    particle[0] = [x + dx for x, dx in zip(particle[0], particle[1])]
    return particle

def first(particles):
    for _ in range(1000):
        particles = map(lambda p: step(p), particles)

    dists = list(map(lambda p: sum(map(abs, p[0])), particles))
    return dists.index(min(dists))

def second(particles):
    for _ in range(1000):
        particles = list(map(lambda p: step(p), particles))

        positions = collections.defaultdict(list)
        for i, p in enumerate(particles):
            positions[tuple(p[0])].append(i)

        collisions = set()
        for lst in positions.values():
            if len(lst) > 1:
                collisions.update(lst)

        particles = [p for i, p in enumerate(particles) if i not in collisions]

    return len(particles)
        
with open('input.in') as f:
    particles = parse(f)
    print(first(copy.deepcopy(particles)))
    print(second(particles))
