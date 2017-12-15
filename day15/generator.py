# given constants
DIV = 2147483647
A_MULT = 16807
B_MULT= 48271

def lowest_bits(x):
    return x & 0xffff

def first(a, b):
    count = 0
    for _ in range(40000000):
        a = (a * A_MULT) % DIV
        b = (b * B_MULT) % DIV
        if lowest_bits(a) == lowest_bits(b): count+=1

    return count

def generator(multOf, factor, x):
    while True:
         x = (x * factor) % DIV
         if x % multOf == 0:
             yield lowest_bits(x)

def second(a, b):
    genA = generator(4, A_MULT, a)
    genB = generator(8, B_MULT, b)
    count = 0
    for _ in range(5000000):
        try:
            if next(genA) == next(genB):
                count+=1
        except StopIteration:
            break
    
    return count
        
# takes 20~ seconds for both
print(first(516, 190))
print(second(516, 190))
