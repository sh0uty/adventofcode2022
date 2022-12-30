from collections import defaultdict

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

commands = [command.replace('$ ', '') for command in data if command != '$ ls' and not command.startswith('dir')]

stack = []
sizes = defaultdict(int)

for i in range(len(commands)):
    line = commands[i]
    if line[0:2] == 'cd' and '..' in line:
        stack.pop()
    elif line[0:2] == 'cd':
        stack.append(i)
    else:
         size = int(line.split(' ')[0])
         for s in stack:
            sizes[s] += size

print(f'Part 1: {sum([sizes[i] for i in sizes if sizes[i] <= 100000])}')

free_space = 70000000 - sizes[0]
free_space_needed = 30000000 - free_space

possible_deletes = [sizes[i] for i in sizes if sizes[i] >= free_space_needed]

print(f'Part 2: {min(possible_deletes)}')