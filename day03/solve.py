from collections import defaultdict

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

total = 0

for line in data:
    middle = int(len(line)/2)
    left = line[:middle]
    right = line[middle:]

    intersecting = set(left) & set(right)
    
    key = intersecting.pop()

    total += ord(key) - 96 if (key >= 'a' and key <= 'z') else ord(key) - 65 + 27

print(f"Part 1: {total}")

total = 0

for i in range(0, len(data), 3):
    first = data[i]
    second = data[i+1]
    third = data[i+2]

    intersecting = set(first) & set(second) & set(third)

    key = intersecting.pop()

    total += ord(key) - 96 if (key >= 'a' and key <= 'z') else ord(key) - 65 + 27

print(f"Part 2: {total}")