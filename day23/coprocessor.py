from math import sqrt; from itertools import count, islice

#https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def get_val(regs, val):
    if val.isalpha():
        return regs[val]
    else:
        return int(val)

def second(instructions):
    b = 108400 # start value b
    c = 125400 # goal value b
    h = 0

    while True:
        # when b is prime we skip set f 0 and thereby skip sub h -1
        if not isPrime(b):
            h += 1
        if b == c: #set g b, sub g c, jnz g 2 -> end condition
            return h
        b += 17

# basically copy of day 18
def first(instructions):
    regs = dict(zip('abzdefgh', [0]*8))
    count = 0
    i = 0
    while 0 <= i < len(instructions):
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
    print(second(instructions))
