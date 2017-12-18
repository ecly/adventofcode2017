def first(instructions):
    regs = {}
    sound = 0
    i = 0
    iterations = 0
    while 0 <= i < len(instructions):
        print(regs)
        instr = instructions[i].split()
        cmd = instr[0]
        print(instructions[i] + " #" + str(i))

        # handle new keys
        if instr[1] not in regs:
            regs[instr[1]] = 0
        if len(instr) == 3 and instr[2] not in regs and instr[2].isalpha():
            regs[instr[2]] = 0

        if cmd == 'snd':
            sound = regs[instr[1]]
        elif cmd == 'set':
            if instr[2].isalpha(): regs[instr[1]] = regs[instr[2]]
            else: regs[instr[1]] = int(instr[2])
        elif cmd == 'add':
            if instr[2].isalpha(): regs[instr[1]] += regs[instr[2]]
            else: regs[instr[1]] += int(instr[2])
        elif cmd == 'mul':
            if instr[2].isalpha(): regs[instr[1]] *= regs[instr[2]]
            else: regs[instr[1]] *= int(instr[2])
        elif cmd == 'mod':
            if instr[2].isalpha(): regs[instr[1]] = regs[instr[1]] % regs[instr[2]]
            else: regs[instr[1]] = regs[instr[1]] % int(instr[2])
        elif cmd == 'rcv':
            if regs[instr[1]] != 0:
                return sound
        elif cmd == 'jgz':
            val = 0
            if instr[1].isalpha(): val = regs[instr[1]]
            else : val = int(instr[1])
            if val > 0:
                offset = int(instr[2])
                i = i + offset
                continue
        i+=1
    return sound


with open('input.in') as f:
    instructions = f.read().splitlines()
    print(first(instructions))
