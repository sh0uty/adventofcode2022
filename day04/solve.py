with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

total = 0

for line in data:
    first, second = line.split(',')
    first_1, first_2 = map(int, first.split('-'))
    second_1, second_2 = map(int, second.split('-'))

    l1 = set(range(first_1, first_2 + 1))
    l2 = set(range(second_1, second_2 + 1))

    if l1.issubset(l2) or l2.issubset(l1):
        total += 1

print(f"Part1: {total}")

total2 = 0

for line in data:
    first, second = line.split(',')
    first_1, first_2 = map(int, first.split('-'))
    second_1, second_2 = map(int, second.split('-'))

    l1 = set(range(first_1, first_2 + 1))
    l2 = set(range(second_1, second_2 + 1))

    if l1.intersection(l2):
        total2 += 1

print(f"Part2: {total2}")