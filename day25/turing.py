STEPS = 12994925
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5

def main():
    tape = {}
    cursor = 0
    state = A
    for _ in range(STEPS):
        val = tape.get(cursor, False)
        if state == A:
            if not val:
                tape[cursor] = True
                cursor += 1
                state = B
            else:
                tape[cursor] = False
                cursor -= 1
                state = F
        elif state == B:
            tape[cursor] = False
            cursor += 1
            state = C if not val else D
        elif state == C:
            tape[cursor] = True
            if not val:
                cursor -= 1
                state = D
            else:
                cursor += 1
                state = E       
        elif state == D:
            tape[cursor] = False
            cursor -= 1
            state = E if not val else D
        elif state == E:
            if not val:
                tape[cursor] = False
                cursor += 1
                state = A
            else:
                tape[cursor] = True
                cursor += 1
                state = C
        elif state == F:
            tape[cursor] = True
            cursor = cursor-1 if not val else cursor+1
            state = A

    return list(tape.values()).count(True)

print(main())
