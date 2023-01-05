import sys

with open('day13/input.txt', 'r') as file:
    data = [x.split('\n') for x in file.read().split('\n\n')]

def compare(t1, t2):
    if isinstance(t1, list) and isinstance(t2, list):
        for entry in zip(t1, t2):
            result = compare(entry[0], entry[1])
            if result == 0:
                continue
            else:
                return result
        if len(t1) > len(t2):
            return 1
        elif len(t2) > len(t1):
            return -1
        else:
            return 0

    if isinstance(t1, int) and isinstance(t2, int):
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
        else:
            return 0

    if isinstance(t1, list):
        t2 = [t2]
    elif isinstance(t2, list):
        t1 = [t1]

    return compare(t1, t2)

    
total = 0

for index, entry in enumerate(data):
    val = compare(eval(entry[0]), eval(entry[1]))
    if val == -1:
        total += index + 1

print(f'Part 1: {total}')


with open('day13/input.txt', 'r') as file:
    data = [eval(line.strip()) for line in file.readlines() if line.strip()]

data += [[2]], [[6]]
ordered = [data.pop(0)]

for entry in data:
    index = 0
    while compare(entry, ordered[index]) == 1:
        index += 1
        if index == len(ordered):
            break
    if index == len(ordered):
        ordered.append(entry)
    else:
        ordered.insert(index, entry)

sol = (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)

print(f'Part 2: {sol}')