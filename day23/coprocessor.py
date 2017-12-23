def get_val(regs, val):
    if val.isalpha():
        return regs[val]
    else:
        return int(val)

def first(instructions):
    regs = dict(zip('abzdefgh', [0]*8))
    count = 0
    i = 0
    while 0 <= i < len(instructions):
        print(i)
        instr = instructions[i].split()
        cmd = instr[0]

        if cmd == 'set':
            regs[instr[1]] = get_val(regs, instr[2])
        elif cmd == 'sub':
            regs[instr[1]] -= get_val(regs, instr[2])
        elif cmd == 'mul':
            count +=1 
            regs[instr[1]] *= get_val(regs, instr[2])
        elif cmd == 'jnz':
            val = get_val(regs, instr[1])
            if val != 0:
                i = i + get_val(regs, instr[2])
                continue
        i+=1
    return count

with open('input.in') as f:
    instructions = f.read().splitlines()
    print(first(instructions))
