def first(step):
    buffer = [0]
    pos = 0
    for i in range(1,2018):
        pos = (pos + step) % i + 1
        buffer.insert(pos, i)

    return buffer[(pos+1)%len(buffer)]

def second(step):
    pos = 0
    val = 0
    for i in range(1,50_000_000):
        pos = (pos + step) % i + 1
        if pos == 1: 
            val = i

    return val

input = 337
print(first(input))
print(second(input))
