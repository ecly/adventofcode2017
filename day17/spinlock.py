def main(step):
    buffer = [0]
    pos = 0
    for i in range(1,2018):
        pos = (pos + step) % len(buffer) + 1
        buffer.insert(pos, i)

    return buffer[(pos+1)%len(buffer)]

print(main(337))
