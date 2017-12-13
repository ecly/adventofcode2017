def read(file):
    firewall = []
    for line in file:
        layer, range = map(str.strip, line.split(':'))
        firewall.append((int(layer), int(range)))
    return firewall
        
def ride(firewall):
    severity = 0
    for _, (l,r) in enumerate(firewall):
        if l%(r*2-2) == 0: severity += l*r
    return severity

def is_caught(firewall, delay):
    for _, (l,r) in enumerate(firewall):
        if (l+delay)%(r*2-2) == 0: return True
    return False

file = open('input.in', 'r')  
firewall = read(file)
print(ride(firewall))

delay = 0
while is_caught(firewall, delay): delay+=1
print(delay)
