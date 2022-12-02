with open('./input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

lookup_table = {
    'A X' : (3, 1),
    'A Y' : (6, 2),
    'A Z' : (0, 3),
    'B X' : (0, 1),
    'B Y' : (3, 2),
    'B Z' : (6, 3),
    'C X' : (6, 1),
    'C Y' : (0, 2),
    'C Z' : (3, 3)
}

lookup_table2 = {
    'A X' : (0, 3),
    'A Y' : (3, 1),
    'A Z' : (6, 2),
    'B X' : (0, 1),
    'B Y' : (3, 2),
    'B Z' : (6, 3),
    'C X' : (0, 2),
    'C Y' : (3, 3),
    'C Z' : (6, 1)
}

total = sum([sum(lookup_table[pair]) for pair in data])
total2 = sum([sum(lookup_table2[pair]) for pair in data])

print(f"Part 1: {total}")
print(f"Part 1: {total2}")
