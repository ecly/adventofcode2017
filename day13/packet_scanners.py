def main(file):
    firewall = []
    for line in file:
        layer, range = map(str.strip, line.split(':'))
        firewall.append((int(layer), int(range)))
        
    severity = 0
    for _, (l,r) in enumerate(firewall):
        if l%((r-1)*2) == 0: severity += l*r

    return severity

with open('input.in', 'r') as file:
    print(main(file))
