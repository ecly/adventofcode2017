from multiprocessing import Process, Queue, Value, Semaphore

def get_val(regs, val):
    if val.isalpha():
        return regs[val]
    else:
        return int(val)


def second(instructions, send, receive, counter, sem, default):
    regs = {}
    i = 0
    while 0 <= i < len(instructions):
        instr = instructions[i].split()
        cmd = instr[0]

        # handle new keys
        if instr[1] not in regs:
            regs[instr[1]] = default
        if len(instr) == 3 and instr[2] not in regs and instr[2].isalpha():
            regs[instr[2]] = default
        if cmd == 'snd':
            send.put(regs[instr[1]])
            sem.release()
            counter.value += 1
        elif cmd == 'set':
            regs[instr[1]] = get_val(regs, instr[2])
        elif cmd == 'add':
            regs[instr[1]] += get_val(regs, instr[2])
        elif cmd == 'mul':
            regs[instr[1]] *= get_val(regs, instr[2])
        elif cmd == 'mod':
            regs[instr[1]] = regs[instr[1]] % get_val(regs, instr[2])
        elif cmd == 'rcv':
            sem.acquire()
            regs[instr[1]] = receive.get()
        elif cmd == 'jgz':
            val = get_val(regs, instr[1])
            if val > 0:
                i += get_val(regs, instr[2])
                continue
        i+=1
    return sound

def solve_second(instructions):
    p0in, p1in = Queue(), Queue()
    p0val, p1val = Value('i', 0), Value('i', 0)
    sem = Semaphore(2)
    p0 = Process(target=second, args=(instructions, p0in, p1in, p0val, sem, 0,))
    p1 = Process(target=second, args=(instructions, p1in, p0in, p1val, sem, 1,))
    p0.start()                                                    
    p1.start()                                                    

    # wait till we're either deadlocked or we're finished
    while(p0.is_alive() and p1.is_alive()):
        if sem.acquire(False): sem.release()
        else: break

    p0.terminate()
    p1.terminate()
    return p1val.value

def first(instructions):
    regs = {}
    sound = 0
    i = 0
    while 0 <= i < len(instructions):
        instr = instructions[i].split()
        cmd = instr[0]

        # handle new keys
        if instr[1] not in regs:
            regs[instr[1]] = 0
        if len(instr) == 3 and instr[2] not in regs and instr[2].isalpha():
            regs[instr[2]] = 0

        if cmd == 'snd':
            sound = regs[instr[1]]
        elif cmd == 'set':
            regs[instr[1]] = get_val(regs, instr[2])
        elif cmd == 'add':
            regs[instr[1]] += get_val(regs, instr[2])
        elif cmd == 'mul':
            regs[instr[1]] *= get_val(regs, instr[2])
        elif cmd == 'mod':
            regs[instr[1]] = regs[instr[1]] % get_val(regs, instr[2])
        elif cmd == 'rcv':
            if regs[instr[1]] != 0:
                return sound
        elif cmd == 'jgz':
            val = get_val(regs, instr[1])
            if val > 0:
                i = i + get_val(regs, instr[2])
                continue
        i+=1
    return sound

with open('input.in') as f:
    instructions = f.read().splitlines()
    print(first(instructions))
    print(solve_second(instructions))
