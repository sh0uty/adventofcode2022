with open('./input.txt') as file:
    data = [x.strip() for x in file.readlines()]

calories = 0
sums = []

for entry in data:
    if not entry:
        sums.append(calories)
        calories = 0
    else:
        calories += int(entry)
         

print(f"Part 1: {max(sums)}")

sums = sorted(sums)

print(f"Part 2: {sum(sums[-3:])}")