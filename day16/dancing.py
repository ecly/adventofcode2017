def main(file):
    l = list('abcdefghijklmnop')
    for m in file.read().split(','):
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
    print(main(f))

