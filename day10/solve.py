with open('day10/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

cycle = 1
reg_x = 1
total = 0

crt = ''

def check_cycle(c, r):
    global crt
    if r <= c % 40 <= r + 2:
        crt += '#'
    else:
        crt += '.'
    if c % 40 == 0:
        crt += '\n'

    if c % 40 == 20:
        return c * r
    return 0

for line in data:
    if line[:4] == 'addx':
        for i in range(2):
            if i == 0:
                cycle += 1
            else:
                reg_x += int(line[5:])
                cycle += 1
            total += check_cycle(cycle, reg_x)
    else:
        cycle += 1
        total += check_cycle(cycle, reg_x)

print(f'Part 1: {total}')
print(f'Part 2: \n{crt}')